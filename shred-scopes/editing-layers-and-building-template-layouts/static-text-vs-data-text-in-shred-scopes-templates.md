# Static Text vs Data Text in Shred Scopes Templates

Static text displays fixed wording at every frame. Data text reads an available telemetry stream and formats its changing value as the timeline moves. Choosing the correct layer type keeps labels stable and measured values synchronized with the GoPro source.

Many templates use both: a data-text layer for a value such as speed and a static-text layer for a label such as "SPEED" or "MPH."

## Open the template

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," load telemetry, and open a template in the Template Editor.

Create a custom copy with "Template" > "Save As New" when changing a built-in design.

## Use static text for fixed wording

Add a "text" layer when the same characters should appear throughout the complete export.

Suitable uses include:

- Metric names such as "SPEED," "ALTITUDE," or "G-FORCE"
- Unit labels such as "MPH," "KM/H," "FT," or "M"
- Titles and captions
- Cardinal-direction letters on a custom compass
- Decorative numbers or words

Static-text controls include the displayed text, font, size, weight, X/Y anchor, alignment, baseline, rotation, fill, stroke, letter spacing, and shadow or glow.

Use "arc·text" instead when fixed wording should follow a circular arc.

## Use data text for changing telemetry

Add a "data·text" layer when the displayed value should update at each timeline frame.

Suitable streams include:

- Speed
- Altitude
- Distance traveled
- Grade
- G-force and acceleration
- GPS course
- Vertical speed
- Cumulative airtime
- Elapsed time or GPS time

After adding the layer:

1. Open its data controls.
2. Select "Stream."
3. Choose a stream available in the active source.
4. Choose "Convert" when another compatible unit is required.
5. Configure number, duration, direction, date, or time formatting as appropriate.
6. Preview several timeline positions.

The stream list is determined by the active telemetry source. A data-text mapping can become unavailable after switching to a source that does not contain it.

## Format a numeric value

Data text can provide controls such as:

- Decimal places
- Leading zeroes
- A plus sign for positive values
- Thousands separators
- Prefixes and suffixes
- Text mapping for value ranges
- Fixed or automatic fitting inside a maximum area

Use a static unit label when the unit should have separate styling or placement. Use a data-text suffix when the value and unit should behave as one text string.

Do not leave a static "MPH" label beside a data value converted to km/h.

## Format time and duration

Elapsed time and cumulative airtime can be formatted as raw seconds or duration styles such as MM:SS and HH:mm:ss, with additional precision where available.

GPS time is an absolute recorded timestamp and has date, clock, time-zone, and 12-hour or 24-hour formatting. It should not be substituted for elapsed duration.

Choose the stream first, then configure the formatting controls appropriate to that stream.

## Control data behavior

Unlike static text, data text can expose input controls such as:

- Smoothing
- Unit conversion
- Clamping
- Deadband
- Range mapping
- Conditional visibility

These affect how the selected layer displays the stream. They do not modify the extracted telemetry used by other layers.

Use smoothing for visual stability, clamping for an intended input limit, and deadband for a neutral window. Preview the full timeline after changing any of them.

## Pair a value with a label

To build a speed readout:

1. Add data text mapped to "Speed 2D (ground)" or "Speed 3D."
2. Convert the value to mph or km/h.
3. Add static text for "SPEED."
4. Add a static unit label if the unit is not a data-text suffix.
5. Align the three layers.
6. Group them if they should move together.

This pattern applies to altitude, distance, grade, vertical speed, and other measurements.

## Plan for changing text width

Static text has predictable characters. Data text can grow or shrink as the value changes.

Preview:

- The smallest value
- The largest value
- Negative and positive values
- Values with a plus sign
- The longest formatted date or time

Use alignment and fitting controls so changing width does not shift the layout unexpectedly. A right-aligned value can keep its unit position more stable, while centered text can expand in both directions.

## Avoid common layer-choice errors

- Do not use static text for a number expected to animate.
- Do not use data text for a label that never changes unless a value-to-text map is intentionally required.
- Do not map a unit label to a telemetry stream.
- Do not assume every source contains the same data-text streams.
- Do not judge data-text fit from only one frame.
- Do not confuse GPS time with elapsed time.

## Save and preview

Play the telemetry preview from beginning to end, checking the relationship between each value and its fixed labels. Save the custom template after units, formatting, alignment, and source compatibility are correct.

The finished layout now uses static text for stable context and data text for values that change with the GoPro telemetry.
