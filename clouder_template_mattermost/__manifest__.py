# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Clouder Template Mattermost',
    'version': '10.0.10.0.0',
    'category': 'Clouder',
    'depends': [
        'clouder',
        'clouder_template_proxy',
        'clouder_template_dns',
    ],
    'author': 'LasLabs Inc.',
    'license': 'LGPL-3',
    'website': 'https://github.com/LasLabs/clouder_templates_mattermost',
    'data': [
        'data/image_template.xml',
        'data/image.xml',
        'data/image_port.xml',
        'data/image_volume.xml',
        'data/application_tag.xml',
        'data/application_type.xml',
        'data/application_template.xml',
        'data/application.xml',
        'data/application_link.xml',
    ],
    'installable': True,
    'application': False,
}
