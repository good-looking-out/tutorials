# How to Choose Fonts for a GoPro Telemetry Overlay

Font selection affects more than the visual character of a GoPro telemetry overlay. Different fonts change the width of numbers, the baseline of labels, the space required by units, and the way text follows an arc. A font that fits one data value can overflow when the telemetry changes.

Shred Scopes can use bundled fonts, common named system fonts, and locally installed fonts available to the browser. The most reliable choice depends on where the template will be edited and exported.

## Understand the font sources

The font picker can present more than one kind of font:

- Bundled fonts are supplied for use in the editor and are the most dependable choice across browsers and computers.
- Named system fonts are common families such as Arial, Georgia, Times New Roman, Courier New, Menlo, Impact, or the current system interface font. Their exact appearance and available weights can vary by operating system.
- Locally installed fonts are fonts present on the current computer. Browser support for finding and listing these fonts varies.

For a template that must be reopened or exported on a different computer, prefer a bundled font. A local font can be suitable when the complete workflow stays on one computer and the license permits its intended use.

## Open the text controls

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the intended template in the Template Editor.

Select a layer that displays type, such as:

- A static text label
- Arc text
- Data text
- Tick labels in a data-ticks layer

Open its font control. A template can use different fonts in different layers, although a limited type system is usually easier to read and maintain.

## 1. Start with the purpose of the layer

Choose the font according to what the layer must communicate:

- Changing numeric values benefit from clear, distinct digits and stable widths.
- Small unit labels need open letterforms that remain recognizable after downscaling.
- Headings can use a more distinctive face if they do not compete with the telemetry.
- Arc labels need characters that remain readable when rotated around a curve.
- Dense tick scales usually need a compact face with legible numbers at small sizes.

Avoid judging a data-text font from a single value. Preview the longest expected positive value, a negative value if applicable, the decimal separator, and every unit or prefix that will appear.

## 2. Choose a bundled font for portability

Select a bundled family when consistent access matters more than matching a font already installed on the computer. Choose an available weight, then wait for the canvas preview to update before changing size or spacing.

Bundled fonts reduce the chance that the browser will substitute another family when a template is opened elsewhere. They are therefore the safer choice for reusable templates and workflows that move between computers or browsers.

## 3. Choose a named system font

Select a named system family when the desired appearance is provided by the current operating system. Check the available weights in the font control rather than assuming every common weight exists.

The same family name can resolve differently across operating systems. A system interface font can also change according to the computer. Review a short export on the computer that will produce the final video.

## 4. Use a locally installed font

Some Chromium-based browsers can list locally installed fonts after the browser grants permission. Use the installed-font refresh or discovery control if it is available, respond to the browser permission prompt, and then choose the family from the resulting list.

If the picker reports that installed fonts are blocked, review the browser's site permissions and refresh the list. If no installed fonts appear, confirm that the font is installed for the current operating-system user and restart the browser if the installation was recent.

Firefox and Safari generally do not provide the same installed-font listing. A local family can still work when its exact family name is known and the interface allows that name to be entered, but the browser may substitute another font if the name is incorrect or unavailable.

Use only fonts whose licenses permit the intended video or commercial use.

## 5. Select a real font weight

Choose a weight that the selected family actually supplies. A browser can sometimes simulate bold or another style when a true font file is unavailable, producing less predictable letter shapes and spacing.

For small telemetry values, medium or semibold weights often survive video compression better than very thin weights. Very heavy weights can make small counters and decimal punctuation difficult to distinguish.

## 6. Refit the layer after the font changes

A font change can alter character widths, ascenders, descenders, and baseline position. Recheck:

- Font size
- Letter spacing
- Line height where available
- Horizontal alignment
- Baseline alignment
- Arc radius, start angle, and character orientation for arc text
- Stroke width and shadow
- Maximum width and height for automatically fitted data text

Do not use extra spaces to correct alignment. Use the layer's position, alignment, and fitting controls so the result remains stable as the value changes.

## 7. Test changing telemetry values

Scrub through the source or play the preview. Check values that contain narrow digits such as 1, wide digits such as 8, a minus sign, a plus sign, decimal places, and thousands separators when enabled.

For fixed-size data text, confirm that the longest value stays inside the canvas and does not overlap nearby layers. For automatically fitted text, verify that the derived size does not shrink so much at extreme values that the reading becomes inconsistent.

When several data-text layers must align in a column, a font with tabular or similarly stable number widths can reduce visible shifting. If the selected font does not provide stable digits, allow additional horizontal space or use separate alignment points.

## 8. Coordinate fonts with a template constant

When several compatible layers should share one family, create a font template constant and select it from each compatible font control. Changing the constant then updates all connected consumers.

A font constant remains local to that template. Selecting a literal font again on one layer disconnects that layer from the shared value.

## 9. Verify against the source and export size

Place the template over the source footage in Source Composite and inspect bright, dark, and detailed frames. Check the type at the intended playback size, not only while the editor is enlarged.

Confirm that:

- Digits remain distinguishable during motion.
- Units are readable without dominating the value.
- Stroke or shadow provides enough separation.
- The selected font is still available after reopening the template.
- A short test export matches the preview.

Save the custom template after the font, weight, fitting, and alignment have been verified.
