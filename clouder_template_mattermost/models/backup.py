# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from os import path

from odoo import api, models


class ClouderBackup(models.Model):
    """ It provides Mattermost context for Clouder Backups

    All public methods and properties are to be prefixed with ``mattermost`` in
    order to prevent namespace clashes with existing operations, unless
    overloading and calling + returning super
    """

    _inherit = 'clouder.backup'

    @property
    def mattermost_volumes_data(self):
        """ It returns a ``clouder.image.volume`` Recordset for data vols """
        res = self.env['clouder.image.volume']
        for volume in ['data', 'etc', 'log']:
            res += self.__get_internal_ref(
                'image_volume_mattermost_%s' % volume,
            )
        return res

    @api.multi
    def deploy_base(self):
        """ It backs up the file store """
        res = super(ClouderBackup, self).deploy_base()
        if self.base_id.application_id.type_id.name == 'mattermost':
            self.mattermost_deploy_base()
        return res

    @api.multi
    def restore_base(self):
        """ It restores a backup of the file store """
        res = super(ClouderBackup, self).deploy_base()
        if self.base_id.application_id.type_id.name == 'mattermost':
            self.mattermost_restore_base()
        return res

    @api.multi
    def mattermost_deploy_base(self):
        """ It backs up the filestore for Mattermost application """
        for volume in self.elasticsearch_volumes_data():
            self.service_id.base_backup_container.execute([
                'rsync', '--progress', '-aze',
                volume.localpath,
                path.join(self.BACKUP_BASE_DIR, self.name, volume.name),
            ],
                username=self.base_id.application_id.type_id.system_user,
            )

    @api.multi
    def mattermost_restore_base(self, base):
        """ It restores a backup of the file store """
        for volume in self.elasticsearch_volumes_data():
            self.service_id.base_backup_container.execute([
                'rsync', '--progress', '-aze', '--delete',
                path.join(self.BACKUP_BASE_DIR, self.name, volume.name),
                volume.localpath,
            ],
                username=self.base_id.application_id.type_id.system_user,
            )

    def __get_internal_ref(self, name):
        return self.env.ref('clouder_template_mattermost.%s' % name)
