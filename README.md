# Mapbox GL Styles

Collection of Mapbox GL styles and sprites. The styles are developed targeting
support for [OSM Scout Server](https://github.com/rinigus/osmscout-server) clients and tiles built using
scripts from https://github.com/rinigus/mapbox-gl-importer . See [README.md](https://github.com/rinigus/mapbox-gl-importer/blob/master/README.md)
for description of the tile schema.


# Support packages

As spritezero is supported in Node.js version 8, install [nvm](https://github.com/nvm-sh/nvm) and use it to get correct packages installed:
```
nvm install 8
nvm use 8
npm install
```

This is needed for generation of sprites and styles.

# Sprites

Icons are based on
[Maki icon set by Mapbox](https://github.com/mapbox/maki) and on icon
set distributed by OpenMapTiles with OSM Bright Style
(https://github.com/openmaptiles/osm-bright-gl-style).

To regenerate sprite set, install `spritezero-cli`:

```
npm install @mapbox/spritezero-cli
```

Generate sprites (used ratio 4):

```
spritezero --ratio 4 sprites/sprite svg
```

Script `bin/make_icons` allows to regenerate all supported icons for OSM Scout Server.


# Styles

Styles are generated using a set of scripts allowing you to use

* variables for definition of colors and other features,
* split layers into smaller subsections and edit them one-by-one.

This approach is similar to CartoCSS when used to generate Mapnik styles.

Each style should be contained in one folder and consists of at least three files:

* `style.json` - Mapbox GL style JSON with its "layers" replaced later by the generated layers. Thus, don't define layers in this file.
* `layers` - space or newline separated list of JSON files defining a subarray with layers definitions. The file names should be given as relative to the style directory.
* `variables.less` - definition of global variables using [LESS](http://lesscss.org/) syntax

In `style.json` and JSON files used to define layers, you could use variables defined in LESS `variables.less` file as `%variable_name%` where this string will be replaced by the variable value as found by LESS processor.

Requirements are

* bash
* node

To make local node scripts available, run `npm install`

When working with styles, run `bin/styler` to generate Mapbox GL style. This script requires style directory as the first argument and the output directory as the second. In addition, it accepts extra arguments that will be passed to [`variable-replacer`](https://github.com/felicienfrancois/node-variable-replacer) as extra arguments. For example,

* `bin/styler styles/src/osmbright/ styles --data-hosturl="http://HOSTNAMEPORT"`

will generate Mapbox GL style compatible with OSM Scout Server where `hosturl` variable is replaced by `http://HOSTNAMEPORT`. As a limitation, it looks like
variable values cannot contain `:` symbol.

Script `bin/make_styles` allows to regenerate all supported styles for OSM Scout Server.


# Testing

It is possible to test developed styles using `maptiler/tileserver-gl` Docker image. After generation of the styles, run `bin/tileserver` with MBTiles file as an argument. It will pick up all styles in `styles` subfolder, use sprites in `sprites`, pull Docker image and serve the maps via it. Port can be specified via `--port` option.

For testing, it is possible to specify path of font glyphs directory with the subfolders of that directory having a font name (option `--glyphs`). That allows to replace fonts provided by Docker image. When developing styles for OSM Scout Server, fonts imported by scripts from https://github.com/rinigus/mapbox-gl-fonts are used.
