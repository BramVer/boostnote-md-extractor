# boostnote-md-extractor
Script to transfer the extract the content from the Boostnote files in cson to md.

## Why
After using Boostnote for a while, I got frustrated by some implementations so I wanted to try Joplin.
I saw that Boostnote did not save my notes as pure markdown but with their custom wrapper and the files had a `.cson` extension.
I could manually export all `.md` files one after the other, or write a script to extract the content and write each file to the desired output directory.

##### Want to use this script too?
Sure, go ahead, but know that I have hardcoded everything.
It looks for `*.cson` files and creates `*.md` files.
The filenames do not get changed (so they contain the same hash from Boostnote),
and the origin/output directory is set in the main method.
Change these to what you need and you'll be good to go I suppose.