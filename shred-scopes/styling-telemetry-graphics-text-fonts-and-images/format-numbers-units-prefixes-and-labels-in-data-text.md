# How to Format Numbers, Units, Prefixes, and Labels in Data Text

A data-text layer turns a GoPro telemetry stream into changing text. Its display format determines whether viewers see a raw-looking value or a clear readout such as `42.7 mph`, `+1.2 G`, or `ALT 2,450 ft`.

Configure the stream and unit conversion before finalizing the text format. The conversion controls what the number means; decimals, signs, separators, prefixes, and suffixes control how that number is presented.

## Open or add a data-text layer

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load a GoPro clip, saved telemetry source, or sample. Open a template in the Template Editor.

Select an existing "data·text" layer, or add one through "Layers" > "Add Layer." Choose the telemetry stream under "Stream," then choose the required unit under "Convert."

Examples include speed converted to mph or km/h, altitude converted to feet or meters, and acceleration converted to G or another supported unit.

## 1. Choose the display format

Open "Display format" and choose a format compatible with the mapped stream. A general numeric readout exposes numeric formatting controls. Specialized streams can offer direction, duration, date, or time formats instead.

Use a general number for measurements such as speed, altitude, grade, or G-force. Use a duration format for elapsed time or airtime. Use date and time formatting for GPS time rather than attempting to reproduce a clock with ordinary numeric controls.

## 2. Set decimal precision

Use "Decimals" to choose how many digits appear after the decimal separator.

Select precision according to the measurement and viewing context:

- Whole numbers are often sufficient for a large speed readout.
- One decimal place can show smaller changes in grade, G-force, or vertical speed.
- Additional decimal places should be used only when the source and purpose justify them.

More decimal places increase text width and can make sensor noise look more important than it is. Preview the result during motion before choosing a final precision.

## 3. Format signs and zeroes

Enable "Show + sign" when positive and negative direction must be explicit. This is useful for acceleration and braking, vertical speed, grade, or signed G-force.

Use zero-fill controls when values must occupy a consistent number of character positions. "Zero fill" sets the width, while "Show filled zeroes" determines whether the leading positions are visibly filled with zeroes.

For example, a three-position value can display `007` instead of `7`. This can suit a dashboard style, but ordinary measurements are usually easier to read without leading zeroes.

Check the exact zero state. A signed display should not imply positive or negative movement when the value is effectively zero.

## 4. Add thousands separators

Enable "Thousands separators" for long values such as elevation, distance, or a large cumulative measurement. Separators can make `12450` easier to parse as `12,450`.

The formatted value becomes wider, so recheck the layer's fitting and alignment after enabling this option.

## 5. Add a prefix and suffix

Use "Prefix" for text that should appear before the changing value. Use "Suffix" for a unit or label that should appear after it.

Examples include:

- Prefix `ALT ` and suffix ` ft`
- Prefix `GRADE ` and suffix `%`
- Suffix ` mph`, ` km/h`, ` m`, ` ft`, or ` G`
- Prefix `TIME ` for an elapsed-time display

Include spaces in the prefix or suffix where separation is required. Preview both positive and negative values so the sign remains next to the number rather than appearing detached from it.

Keep the suffix consistent with the selected conversion. Converting speed to kilometers per hour while retaining an `mph` suffix produces a misleading overlay.

## 6. Decide between an attached label and a separate layer

A prefix or suffix moves and fits as part of the changing data text. This is useful when the complete readout should act as one element.

Use a separate static text layer when:

- The label needs a different font, weight, size, or color.
- The unit must stay fixed while the number changes width.
- Several values must align in a table.
- The label needs independent positioning or animation.

If separate layers are used, group them after alignment so the complete readout can be moved without losing its layout.

## 7. Map numeric ranges to words

When the data-text controls offer "Text map," ranges can display words instead of the original number. This can turn a value into labels such as `BRAKING`, `COASTING`, or `ACCELERATING`.

Configure each range and its text, then use hysteresis or hold-frame controls where available to prevent the label from rapidly switching near a boundary. Make the ranges complete enough to cover expected values and confirm which text appears outside them.

A text map changes presentation; it does not change the underlying telemetry or the behavior of another layer mapped to the same stream.

## 8. Control width and fitting

Changing values do not always occupy the same space. Choose fixed sizing when the font size must remain constant and enough canvas space is available. Choose automatic fitting when the text must remain inside a maximum width or height.

For automatic fitting:

1. Set the maximum width and height.
2. Preview the shortest and longest expected values.
3. Observe the derived font size.
4. Confirm that the text does not become too small at an extreme value.

Check alignment and baseline after the format changes. Right alignment can keep a unit column stable, while centered text expands in both directions.

## 9. Preview edge cases

Scrub the timeline and inspect:

- Zero and near-zero values
- The minimum and maximum values
- Positive and negative values
- Values that gain another digit
- Values with decimal and thousands separators
- Data gaps or unavailable states
- Converted units and their suffixes

Also view the template over the original footage in Source Composite. Ensure that the extra width from prefixes and suffixes does not collide with another layer or leave the canvas.

## 10. Save the formatted template

Use "Save" for an existing custom template or "Template" > "Save As New" for a new version. Reopen the saved template and verify that the stream, conversion, numeric format, prefix, suffix, and fitting settings produce the intended readout.
