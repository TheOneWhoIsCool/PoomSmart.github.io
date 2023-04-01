emoji = [
    {
        "file": "emojiport10resources",
        "title": "emojiport10resources",
        "min_ios": "10.0",
        "changes": [
            ["1.4.2", "Updated to iOS 16.4 assets"],
            ["1.3.2", "Updated to iOS 16 assets"]
        ],
        "description": "<p>Up-to-date emoji assets (bitmap, localization, metadata) specific to iOS 10 and above.</p>"
    },
    {
        "file": "emojiattributes",
        "title": "EmojiAttributes",
        "min_ios": "5.1",
        "changes": [
            ["1.7.0~b2", [
                    "Initial support for iOS 16.4 beta emojis",
                    "Fixed installation issue on readonly filesystems devices",
                    "Fixed new emojis displayed as ? on iOS 10 and lower"
            ]],
            ["1.6.0~b2", [
                    "Rootless jailbreak support",
                    "Corrected function finder for iOS 8.2 arm64 and similar"
            ]],
            ["1.5.0", "Stable version"]
        ],
        "description": "<p>Various under-the-hood fixes for emoji display. See <a href=\"https://github.com/PoomSmart/EmojiAttributes/blob/master/README.md\">here</a> for more information.</p>"
    },
    {
        "file": "emojifontmanager",
        "title": "EmojiFontManager",
        "min_ios": "6.0",
        "changes": [
            ["1.3.1", "Simplified hooks, fixing app crash on Fugu15 Max environment"],
            ["1.3.0", [
                "Added rootless support",
                "Removed libcephei installation requirement"
            ]],
            ["1.2.1", "Display total disk space used for all installed fonts"],
            ["1.1.8", "Minor cleanup (Note: XinaA15 jailbreak cannot yet inject into WebContent processes which means EFM will not work in Safari)"]
        ],
        "description": "<p><b>**EmojiPort needs to be installed if you also want new emojis.**</b><br/>\
            This tweak allows you to theme emoji font wihout touching filesystem.\
            Access <b>Settings app &gt; EmojFontManager</b> to choose your font.<br/>\
            EFM fonts must be in this format: <code>(/var/jb)/Library/Themes/EmojiFontManager/&lt;Font-Name&gt;.font/AppleColorEmoji@2x.ttc</code><br/>\
            It is highly recommended to respring after you change the font.</p>"
    },
    {
        "file": "efmfontdl",
        "title": "EFM Font Downloader",
        "changes": [
            ["1.0.3", "Fixed path logic"]
        ],
        "description": "<p>A simple shell script to download an emoji font for EFM from GitHub releases.</p>"
    },
    {
        "file": "emojilayout",
        "title": "EmojiLayout",
        "min_ios": "6.0",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            ["1.2.0", "Compiled with ARC, iOS 6 minimum compatibility as of this version"],
            ["1.1.21", "Recognizes iPad emoji landscape keyboard variant"]
        ],
        "description": "<p>Layout emoji keyboard. Specifically, set number of rows and columns of emoji display.</p>"
    },
    {
        "file": "emojilibrary",
        "title": "EmojiLibrary",
        "min_ios": "5.1",
        "changes": [
            ["1.5.0", "iOS 16.4 beta emojis support"],
            ["1.4.0", "iOS 15.4 emojis support"]
        ],
        "description": "<p>EmojiLibrary is a developer library, and the master library for most of PoomSmart's Emoji tweaks, including\
                    algorithms and functionalities that handle any kind of emojis - display as images properly. Developers\
                    that want to create emoji-related tweaks would find this useful.</p>"
    },
    {
        "file": "emojiport_5_1",
        "title": "EmojiPort (iOS 5.1)",
        "min_ios": "5.1",
        "max_ios": "5.1.1",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            ["1.0.10", "Adopted fixes related to emoji split keyboard from EmojiPort (iOS 6.0-8.2)"]
        ],
        "description": "<p>Latest emojis for iOS 5.1</p>\
            <p>This EmojiPort variant ports some of the iOS 6 variant for best compatibility on iOS 5. The manual way is recommended, as written in <a href=\"https://poomsmart.github.io/emojiport\">here</a>.</p>"
    },
    {
        "file": "emojiport_6",
        "title": "EmojiPort (iOS 6.0 - 8.2)",
        "min_ios": "6.0",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "description": "<p>Latest emojis for iOS 6.0 - 8.2</p>\
                <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_8_9",
        "title": "EmojiPort (iOS 8.3 - 9.3)",
        "min_ios": "8.3",
        "max_ios": "9.3.6",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            ["1.7.0", "Combined with EmojiPort (iOS 8.3 - 8.4)"]
        ],
        "description": "<p>Latest emojis for iOS 8.3 - 9.3</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_10",
        "title": "EmojiPort (iOS 10.0 - 11.4)",
        "min_ios": "10.0",
        "max_ios": "11.4.1",
        "strict_range": True,
        "changes": [
            ["1.3.7", "Added fixup for older iOS where handshake emoji doesn't get skinned"]
        ],
        "description": "<p>Latest emojis for iOS 10.0 - 11.4</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_12",
        "title": "EmojiPort (iOS 12.0 - 16.3)",
        "min_ios": "12.0",
        "max_ios": "16.3.1",
        "strict_range": True,
        "featured_as_banner": True,
        "changes": [
            ["1.4.1", [
                "Allow installation on iOS 15.4 - 16.3.1",
                "Fixed app crash on rootful palera1n devices"
            ]],
            ["1.3.0~b3", [
                "Allow installation on iOS 15.0 - 15.3.1",
                "Improved rootless jailbreak compatibility"
            ]],
            ["1.2.5", "Added missing hook for search engine override lists"]
        ],
        "description": "<p>Latest emojis for iOS 12.0 - 16.3</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojisearchforipad",
        "title": "Emoji Search for iPad",
        "min_ios": "14.0",
        "max_ios": "14.4.2",
        "strict_range": True,
        "screenshots": True,
        "description": "<p>Enable emoji search on iPadOS 14.0 - 14.4</p>"
    },
    {
        "file": "emojifontefm",
        "title": "AppleColorEmoji Unicode 15.0 (EFM)",
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Unicode 15.0 (iOS 16.4) Apple's AppleColorEmoji font for EmojiFontManager.</p><br/>\
            <p>Regular version of this font has all emoji images in PNG format and better compressed than Apple's EMJC image compression.</p><br/>\
            <p>HD version of this font includes additional 160x160 PNG emoji images. They work best if you like large emojis.</p>"
    },
    {
        "file": "emojifontlqefm",
        "title": "AppleColorEmoji Low Quality (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>It's your usual AppleColorEmoji font but low quality. But Why? To save you some disk space? To improve your device performance? To show off your friends?</p><br/>\
            <p>All not quite. It's because sometimes you need not a high quality work to cause <a href=\"https://www.youtube.com/watch?v=7Qxa19ODUIQ\">a global impact such as this one</a>.</p><br/>\
            <p>Unicode version will be in sync with the regular Apple emoji font.</p>"
    },
    {
        "file": "blobmojiefm",
        "title": "Blobmoji Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Blobmoji emoji font (Blobified version of Google Noto Emoji) for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://github.com/C1710/blobmoji/blob/main/LICENSE\">here</a> for licensing.</p>"
    },
    {
        "file": "fbemojiefm",
        "title": "Facebook Emoji Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Facebook emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>"
    },
    {
        "file": "fluentuiefm",
        "title": "FluentUI Emoji Unicode 14.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["14.0.5", "Theme 00a9 and 00ae emojis"]
        ],
        "description": "<p>Windows 11 FluentUI emoji font for EmojiFontManager (Unicode 14.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p>"
    },
    {
        "file": "joypixelsefm",
        "title": "JoyPixels Emoji Unicode 14.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["14.0.5", "Theme 00a9 and 00ae emojis"]
        ],
        "description": "<p>JoyPixels 7.0.1 emoji font for EmojiFontManager (Unicode 14.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://joypixels.com/licenses/free\">here</a> for licensing.</p>"
    },
    {
        "file": "joypixelsdecalefm",
        "title": "JoyPixels Decal Emoji Unicode 14.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["14.0.5", "Theme 00a9 and 00ae emojis"]
        ],
        "description": "<p>JoyPixels 7.0.1 emoji font (with Decal) for EmojiFontManager (Unicode 14.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://joypixels.com/licenses/free\">here</a> for licensing.</p>"
    },
    {
        "file": "notoemojiefm",
        "title": "Noto Color Emoji Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.1", "Included 160x160 PNG images by default"],
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Google Noto Color emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/googlefonts/noto-emoji/blob/main/LICENSE\">here</a> for licensing.</p>"
    },
    {
        "file": "notoemojicursedefm",
        "title": "Noto Color Emoji Cursed Unicode 15.0 (EFM)",
        "description": "<p>Google Noto Color Cursed emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Try it for yourself... it's cursed.</p>"
    },
    {
        "file": "openmojiefm",
        "title": "OpenMoji Unicode 14.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["14.0.4", "Theme 00a9 and 00ae emojis"]
        ],
        "description": "<p>OpenMoji emoji font for EmojiFontManager (Unicode 14.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://github.com/hfg-gmuend/openmoji/blob/master/LICENSE.txt\">here</a> for licensing.</p>"
    },
    {
        "file": "oneuiefm",
        "title": "Samsung One UI 5.0 Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Samsung One UI 5.0 emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p>"
    },
    {
        "file": "tossfaceefm",
        "title": "Toss Face Unicode 14.0 (EFM)",
        "screenshots": True,
        "description": "<p>Toss Face (토스페이스) emoji font for EmojiFontManager (Unicode 14.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://toss.im/tossface\">here</a> for licensing.</p>"
    },
    {
        "file": "twemojiefm",
        "title": "Twemoji Unicode 14.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["14.0.4", "Theme 00a9 and 00ae emojis"]
        ],
        "description": "<p>Twitter Twemoji emoji font for EmojiFontManager (Unicode 14.0).</p>"
    },
    {
        "file": "whatsappefm",
        "title": "WhatsApp Emoji Unicode 14.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["14.0.2", "Optimizing PNG images further with oxipng"]
        ],
        "description": "<p>WhatsApp emoji font for EmojiFontManager (Unicode 14.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p>"
    },
]
