# PA STEELS Standards Finder

A free, independent, searchable reference for all 370 Pennsylvania STEELS standards (K–12), broken into Know, Do, and Think. Built by Amanda Jeane Strode. The standards themselves are written and adopted by the Pennsylvania Department of Education.

## Publish with GitHub Pages
1. Create a new public repository (for example `steels-finder`) and upload everything in this folder.
2. In the repository, go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`, and save.
4. After a minute or two, the site is live at `https://<your-username>.github.io/steels-finder/`.
5. Optional: add a custom domain in the same Pages settings.

## Making changes
The page is generated from the files in `src/`:

| File | What it holds |
|---|---|
| `template.html` | Layout, styles, and all page code. Colors and fonts are set at the top of the `<style>` block. |
| `raw_data.txt` | Standard codes and text, grouped by strand (`## Strand name`). A `*` before the text marks an ETS standard. |
| `tags_final.txt` | `code|Do|Think` tags for each standard. |
| `pdf_data.txt` | `code|id` for each official Foundation Box PDF on SAS. |
| `glossary.js` | Glossary terms and definitions. |
| `pe_map.b64` | The performance expectation diagram (base64 JPEG). |

After editing anything in `src/`, run `python3 build.py` to regenerate `index.html`, then commit both.

### Tag codes
Do (Science & Engineering Practices): AQ, MOD, INV, DATA, MATH, CEDS, ARG, INFO
Think (Crosscutting Concepts): PAT, CE, SPQ, SYS, EM, SF, SC
Think (T&E Practices): ST, CR, MD, CT, OP, CO, CM, ET

## Sources
All standard content comes from PDE's STEELS documents on the Standards Aligned System: https://www.pdesas.org/Page/Viewer/ViewPage/58
