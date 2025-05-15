{
    'name': 'SUN Web Responsive',
    "author":"AMS, Sun Academy",
    'category': 'Hidden',
    'version': '1.0',
    'depends': ['web', 'base_setup'],
    'auto_install': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'sun_web_responsive/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'sun_web_responsive/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'sun_web_responsive/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'sun_web_responsive/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'sun_web_responsive/static/src/webclient/home_menu/home_menu_background.scss', # used by login page
            'sun_web_responsive/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'sun_web_responsive/static/src/webclient/**/*.scss',
            'sun_web_responsive/static/src/views/**/*.scss',

            'sun_web_responsive/static/src/core/**/*',
            'sun_web_responsive/static/src/webclient/**/*.js',
            ('after', 'web/static/src/views/list/list_renderer.xml', 'sun_web_responsive/static/src/views/list/list_renderer_desktop.xml'),
            'sun_web_responsive/static/src/webclient/**/*.xml',
            'sun_web_responsive/static/src/views/**/*.js',
            'sun_web_responsive/static/src/views/**/*.xml',

            # Don't include dark mode files in light mode
            ('remove', 'sun_web_responsive/static/src/**/*.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'sun_web_responsive/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'sun_web_responsive/static/src/scss/primary_variables.scss', 'sun_web_responsive/static/src/scss/primary_variables.dark.scss'),
            ('before', 'sun_web_responsive/static/src/**/*.variables.scss', 'sun_web_responsive/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'sun_web_responsive/static/src/scss/secondary_variables.scss', 'sun_web_responsive/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'sun_web_responsive/static/src/scss/bootstrap_overridden.scss', 'sun_web_responsive/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss',
             'sun_web_responsive/static/src/scss/bs_functions_overridden.dark.scss'),
            # assets_backend
            'sun_web_responsive/static/src/**/*.dark.scss',
        ],
    },
    "license": "LGPL-3",
    "images": ["static/description/img.png"],
}
