# How to Convert Telemetry Units in Shred Scopes

Shred Scopes stores each supported telemetry stream in a default unit and offers compatible conversions at the individual layer input. Conversion changes how that layer displays and maps the value; it does not alter the extracted GoPro telemetry.

Set the conversion before configuring clamps, deadband, fixed ranges, labels, or ticks.

## Common stream conversions

| Stream | Default unit | Available examples |
| --- | --- | --- |
| Speed 2D and Speed 3D | m/s | mph, km/h, knots, min/km, min/mi, ft/min |
| Altitude | m | ft, yd, mi, km |
| Distance traveled | m | ft, yd, mi, km |
| Vertical speed | m/s | mph, km/h, knots, min/km, min/mi, ft/min |
| GPS-path acceleration | m/s² | ft/s² |
| Grade | percent | signed degrees or absolute steepness in degrees |
| Cumulative altitude gain or loss | m | ft, yd, mi, km |

Some streams, including G-force, camera-axis acceleration, GPS course, GPS path, and rotation rate, do not offer another unit.

## 1. Load the source and template

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Load the intended telemetry and open a template. Select the data-text, data-graphic, or data-ticks layer whose unit should change.

Create a custom copy with "Template" > "Save As New" before retaining changes to a built-in design.

## 2. Choose the stream first

Open the layer's data or input controls and select "Stream." Choose the required measurement before using "Convert."

Conversion choices depend on the stream. A speed layer offers speed and pace units, while altitude offers distance units. If "Convert" has no alternate choices, that stream remains in its default unit.

## 3. Select the conversion

Open "Convert" and choose the finished display unit.

Examples:

- Convert speed to mph for an imperial speedometer.
- Convert speed to km/h for a metric road or riding display.
- Convert altitude to feet or meters.
- Convert distance to miles or kilometers for a long route.
- Convert vertical speed to feet per minute or keep meters per second.
- Convert acceleration to feet per second squared when required.

Choosing "none" retains the stream's default unit.

## 4. Update every related layer

A template can use the same measurement in several places:

- Numeric data text
- Gauge or pointer
- Data ticks
- Running maximum or minimum text
- Static unit label

Set compatible conversions across the complete component. A gauge mapped in m/s should not sit beside tick labels in mph unless the mapping was deliberately coordinated.

Static text does not update when a conversion changes. Replace "MPH" with "KM/H," "FT" with "M," or another correct label manually.

## 5. Reconfigure numeric formatting

Changing units can change the number's magnitude and width. After conversion:

- Review decimal places.
- Check thousands separators.
- Inspect prefixes and suffixes.
- Preview the longest expected value.
- Adjust automatic fitting or font size.

For example, a distance in meters can use a larger whole number than the same distance in kilometers. A text box that fit the kilometer value may not fit meters.

## 6. Reconfigure the range

Range controls use the converted unit. If a fixed speed range was 0–60 mph and the layer changes to km/h, enter a suitable kilometer-per-hour range rather than leaving the old numeric limits.

The same rule applies to:

- "Clamp min" and "Clamp max"
- Deadband width and center
- Fixed input minimum and maximum
- Tick minimum, maximum, and step
- Visibility thresholds

Conversion occurs before these controls.

## 7. Understand pace conversions

Speed streams can display minutes per kilometer or minutes per mile. Pace is an inverse representation: faster movement produces a smaller time-per-distance number.

Use a template designed for pace or review the graphic direction and range carefully. A speedometer whose pointer assumes larger values mean faster movement may need different mapping when showing pace.

## 8. Convert grade correctly

Grade uses percent by default. It can be converted to:

- Signed degrees, which preserve uphill and downhill direction
- Absolute steepness in degrees, which remove the sign

Do not retain a percent symbol after converting to degrees. Do not use absolute steepness when the template must distinguish climbing from descending.

## 9. Preview and verify

Scrub to several values and check:

- The converted number is plausible.
- All text, graphics, and ticks agree.
- Unit labels are correct.
- Fixed ranges and clamps were updated.
- Signed direction still has the intended meaning.
- Text remains inside the canvas.

Changing a unit does not improve missing or noisy source telemetry. It only changes the representation of the value.

## 10. Save the converted template

Save the custom template after every related layer and label uses the intended unit. Use a template name that identifies the unit system when both imperial and metric versions will be retained.

The overlay now displays the active telemetry in a consistent, correctly labeled unit across its values, graphics, and scales.
