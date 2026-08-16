# How to Reuse Colors, Fonts, Text, and Numbers with Template Constants

Template constants are named values that belong to one Shred Scopes template. They make it possible to coordinate compatible controls from a single place instead of repeating the same value throughout a design.

A template constant can be a color, font, number, or text value. Color and font constants can be selected directly by compatible layer controls. Number and text constants are primarily used to supply compatible variables exposed by nested template layers.

## Plan the shared values

Before adding constants, identify values that represent a deliberate part of the template's design system. Useful examples include:

- Primary accent color
- Background color
- Label font
- Numeric font
- Gauge limit passed to a nested template
- Unit or title passed to a nested template

Do not create a constant for every isolated setting. A constant is most useful when two or more consumers should remain synchronized or when a reusable parent template should expose a clear customization point.

## Open Template Constants

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open a custom template in the Template Editor.

Create a custom copy with "Template" > "Save As New" if the starting point is a built-in template. Then open "Template Constants."

## 1. Create a constant

1. Select "Add constant."
2. Enter a clear "Display name," such as `Accent Color`.
3. Review the generated or entered "Variable name."
4. Choose "Color," "Font," "Number," or "Text."
5. Enter or select the initial value.
6. Select "Create."

The variable name must begin with a letter or underscore, contain only letters, numbers, and underscores, and be unique within the template. Use stable names because nested template variables identify the constants available to them.

The display name can be readable and descriptive. The variable name should be concise and durable, such as `accent_color` or `label_font`.

## 2. Reuse a color constant

Select a layer and open a compatible fill, stroke, background, or paint control. Choose the template-constant option, then select the color constant.

Repeat this for every control that should remain connected. For example, one accent constant can control a gauge progress arc, a pointer, and a data-text fill.

Not every paint control necessarily offers every paint source. If a constant option is absent, that particular control does not accept the shared value in its current mode.

To disconnect one control, choose a literal color or another paint type. That layer then retains its own value when the constant changes.

## 3. Reuse a font constant

Select a text, arc-text, data-text, or compatible tick-label control. Open the font picker, choose the template-constant option, and select the font constant.

Connect the font constant to each layer that belongs to the same type system. Size, weight, spacing, and alignment remain separate layer settings unless their controls provide another shared mechanism.

After connecting a font, inspect every linked layer. The same family can require different fitting or sizing for a large value, a small unit label, and curved text.

## 4. Use number and text constants where supported

Ordinary number and text input boxes do not generally provide a direct constant picker. Number and text constants are currently most useful when a nested child template exposes a compatible number or text variable.

For example, a parent can provide:

- A shared maximum gauge value as a number
- A shared unit abbreviation as text
- A shared panel title as text
- A shared scale factor exposed by several child templates

Select the nested template layer, open "Template Variables," set the compatible child variable to "From parent," and choose the parent constant.

## 5. Update a shared value

Return to "Template Constants" and edit the constant's value. Every consumer that remains linked should update.

After a color change, check fills, strokes, transparency, and contrast. After a font change, check widths, baselines, arcs, and automatic fitting. After a number or text change, check every nested child that receives it.

If one layer does not update, select its control and confirm that it still points to the constant rather than a literal value.

## 6. Use constants with several nested templates

A parent template can coordinate multiple child templates through matching variables. For example, separate speed, altitude, and G-force children can receive the same accent color and font from parent constants.

Each child variable must have the same type as the chosen parent constant. A color variable can use only a color constant, and a number variable can use only a number constant.

The constant changes the connected value, but it does not merge the children or alter their internal layout.

## 7. Rename or remove a constant carefully

Review all consumers before changing the role of a constant. A name such as `warning_color` should not later be reused for an unrelated background value merely because it already exists.

To remove a constant:

1. Replace or clear every connected layer control and nested variable.
2. Return to "Template Constants."
3. Select "Remove constant."
4. Use the removal control for the intended constant.
5. Select "Done."

A constant cannot be removed while the template still uses it. This prevents connected controls from being left without a value.

## 8. Remember the template boundary

Constants belong to one template. Creating `Accent Color` in one custom template does not automatically make it available to another unrelated template.

To reuse a coordinated system across multiple designs, use a parent template with nested children, or create constants with consistent names and values separately in each template.

## 9. Preview and save

Test the template over representative source footage and change each constant once to confirm its full effect. Check for a layer that was unintentionally linked or left disconnected.

Use "Save" for an existing custom template or "Template" > "Save As New" for a new version. The saved template retains its constants and the compatible controls or nested variables connected to them.
