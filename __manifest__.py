# -*- coding: utf-8 -*-
{
    'name': "Studio Warning",
    'category': 'Customizations',
    'author': "Francisco Sulé, Witdata",
    'version': '1.0',
    'depends': ['base', 'web','web_studio', 'mail'],
    'data': [
        'data/studio_config_data.xml',
    ],

    'assets': {
              'web.assets_backend': [
                  'studio_warning/static/src/js/studio_systray_patch.js',
              ],
          },
    'application': True,
    'installable': True,
    'auto_install': ['web_studio'],
    'license': 'LGPL-3',
}
