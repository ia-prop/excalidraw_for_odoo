# Copyright (c) 2026 IA-PROP (I.A-PROP SPA, Chile) <contacto@ia-prop.com>. All rights reserved.
# Originally designed and developed by Victor Bastías Escobar <victor.bastiasescobar@gmail.com> (https://vicbas.com).
# All economic rights over this module were assigned to IA-PROP (https://ia-prop.com) in November 2026.
# Authorship attribution to Victor Bastías Escobar is permanent and may not be removed.
# See COPYRIGHT.md for the full copyright and intellectual property notice.
# Third-party exceptions: see "Third-Party Exceptions for This Module" in COPYRIGHT.md.

# Odoo __manifest__.py must be a bare dict literal (read via ast.literal_eval);
# the "useless/unused expression" warnings are unavoidable false positives,
# suppressed below for both ruff (B018) and Pyright.
# pyright: reportUnusedExpression=false
{  # noqa: B018
    "name": "Excalidraw for Odoo",
    "version": "19.0.2.0.3",
    "category": "Productivity",
    "summary": "Excalidraw drawing tool in the record chatter",
    "description": """
Excalidraw for Odoo
===================

Embeds the Excalidraw whiteboard (https://excalidraw.com) as a chatter tool,
fully self-hosted (no CDN required).

Features
--------
* Pencil button in every record chatter opens a drawing picker and a
  fullscreen editor; drawings are stored on the host record.
* Each drawing persists as an editable .excalidraw scene JSON plus a PNG
  render (an ir.attachment pair on the host record).
* Autosave: 45 s inactivity debounce, 60 s max-latency guard, flush on
  dialog close; concurrent saves are last-write-wins.
* Built-in Excalidraw export dialog (PNG / SVG) and .excalidraw file import.
* Permission model: Users (create/edit) and Managers groups gate the tool.
* Vendored library: @excalidraw/excalidraw 0.18.1 (MIT) bundled with esbuild,
  fonts served locally via window.EXCALIDRAW_ASSET_PATH.

Breaking change (19.0.2.0.0)
---------------------------
The standalone "Excalidraw" application and its drawing model were removed.
Updating permanently destroys previously stored standalone drawings (they
are not migrated). Security groups are kept (they gate the new chatter
tool). Note: Odoo keeps the old table on update — see the README deploy
runbook to drop it explicitly and reclaim the space.
        """,
    'author': 'Victor Bastías Escobar <victor.bastiasescobar@gmail.com> (https://vicbas.com)',
    'website': 'https://ia-prop.com',
    'support': 'contacto@ia-prop.com',
    'maintainer': 'IA-PROP — I.A-PROP SPA, Chile <contacto@ia-prop.com> (https://ia-prop.com)',
    "license": "LGPL-3",
    "depends": [
        "web",
        "mail",
    ],
    "data": [
        "security/excalidraw_security.xml",
    ],
    "images": [
        "static/description/thumbnail.png",
    ],
    "assets": {
        "web.assets_backend": [
            # Chatter tool (design §3). static/lib/** stays out of the
            # bundles — loaded via dynamic import, IR-ASSET-1:
            "excalidraw_for_odoo/static/src/js/excalidraw_loader.js",
            "excalidraw_for_odoo/static/src/js/excalidraw_dialogs.js",
            "excalidraw_for_odoo/static/src/js/chatter_patch.js",
            "excalidraw_for_odoo/static/src/xml/chatter_patch.xml",
            "excalidraw_for_odoo/static/src/scss/excalidraw_chatter.scss",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
