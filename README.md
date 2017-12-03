# Mapbox GL Styles

Collection of Mapbox GL styles, sprites, and fonts. The styles are developed targeting 
support for [OSM Scout Server](https://github.com/rinigus/osmscout-server) clients.


# Glyphs

Import fonts into SQLite database using `fontimport.py`
script. Currently imported fonts are Noto fonts as packaged and
patched by Klokantech at
https://github.com/openmaptiles/fonts/tree/master/klokantechnoto :

```
./fontimport.py thirdparty/omt-fonts/klokantechnoto glyphs.sqlite
```


As a requirement, font import requires
[node-fontnik](https://github.com/mapbox/node-fontnik/). Install it
with

```
npm install -g fontnik
```


# Sprites

Icons are based on
[Maki icon set by Mapbox](https://github.com/mapbox/maki) and on icon
set distributed by OpenMapTiles with OSM Bright Style
(https://github.com/openmaptiles/osm-bright-gl-style).

To regenerate sprite set, install `spritezero-cli`:

```
npm install -g @mapbox/spritezero-cli
```

Generate sprites (used ratio 4):

```
spritezero --ratio 4 sprites/sprite svg
```

