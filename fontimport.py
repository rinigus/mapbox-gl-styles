#!/usr/bin/env python2.7

import re, argparse, os, glob, sqlite3, tempfile, shutil

parser = argparse.ArgumentParser(description='Import fonts from given directory into SQLite database as PBF glyphs')
parser.add_argument('fonts_dir', type=str,
                    help='Directory containing TTF and OTF fonts')
parser.add_argument('export_db', type=str, help='SQLite database where the fonts are inserted')

args = parser.parse_args()

def font(filename):
    # from https://stackoverflow.com/a/199126
    f = os.path.basename(re.sub(r"([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))", r"\1 ", filename.replace('-','')[:-4]))
    return f

############
### main ###

conn = sqlite3.connect(args.export_db)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS fonts(stack TEXT NOT NULL, range TEXT NOT NULL, pbf BLOB, unique(stack,range))")

for ext in ["ttf", "otf"]:
    for filename in glob.glob(args.fonts_dir + "/*" + ext):
        fontname = font(filename)
        print filename, fontname
        d = tempfile.mkdtemp()
        os.system("build-glyphs '%s' '%s'" % (filename, d))

        for pbfname in glob.glob(d + "/*pbf"):
            rng = os.path.basename(pbfname)[:-4]
            with open(pbfname, 'rb') as f:
                c.execute("INSERT OR REPLACE INTO fonts(stack,range,pbf) VALUES(?,?,?)", (fontname, rng, buffer(f.read())))

        shutil.rmtree(d)
        
c.execute("CREATE INDEX IF NOT EXISTS idx_fonts ON fonts(stack,range)")
conn.commit()
conn.close()

