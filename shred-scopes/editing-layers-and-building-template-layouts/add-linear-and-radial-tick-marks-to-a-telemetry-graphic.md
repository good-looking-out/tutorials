# How to Add Linear and Radial Tick Marks to a Telemetry Graphic

Tick layers create the marked scales used around gauges, speedometers, bars, and measured displays. Shred Scopes provides fixed or telemetry-derived ticks in both linear and radial layouts.

Choose a tick type whose geometry and numeric range agree with the graphic it accompanies.

## Understand the four tick choices

The layer picker separates:

- Static linear ticks
- Static radial ticks
- Data linear ticks
- Data radial ticks

Static ticks use an entered minimum and maximum that do not depend on telemetry. Data ticks can use a numeric telemetry stream to derive the displayed scale.

Use static ticks for a fixed 0–100 speedometer shared across several videos. Use data ticks when the scale should adapt to the active source's recorded range.

## Open the template and add ticks

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the template.

Then:

1. Open "Layers."
2. Select "Add Layer" or "Add layer here."
3. Choose the required ticks or data-ticks layer.
4. Select linear or radial geometry.
5. Add the layer and give it a descriptive name.

Place the tick layer behind a moving needle or progress marker but in front of the gauge background when that order matches the design.

## Configure linear geometry

Linear tick controls include:

- Center X and Center Y
- Length
- Rotation
- Tick side
- Label side and offset
- Label rotation mode and angle

Use a horizontal line for a bar or timeline-like gauge. Rotate it for a vertical or diagonal display.

Set tick side to place marks above, below, across, or on both sides of the guide line. Position labels on the side with enough room for the largest value.

## Configure radial geometry

Radial tick controls include:

- Center X and Center Y
- Radius
- Arc gap
- Rotation
- Tick direction
- Label radius and orientation
- Automatic label flipping
- Full-circle endpoint behavior

Match the center, radius, arc gap, and rotation to the accompanying needle or arc graphic. Small differences can make the scale appear disconnected from the gauge.

Use automatic label flipping when labels following the arc would otherwise appear upside down.

## Set a static range

For static ticks:

1. Enter the minimum value.
2. Enter the maximum value.
3. Choose whether increasing values run in the normal or reversed direction.
4. Enable "Nice scale" when rounded boundaries and steps are preferred.

Use the same range on the data graphic or needle. A pointer mapped from 0–60 should not sit over ticks labeled 0–100 unless that difference is intentional.

## Derive a range from telemetry

For data ticks:

1. Select "Stream."
2. Choose an available numeric stream.
3. Select the required unit conversion.
4. Set "Bounds source" to use the stream when the scale should adapt.
5. Add minimum or maximum padding if the endpoints need breathing room.
6. Enable "Include zero" when zero must remain on the scale.
7. Enable "Symmetric around zero" for signed values such as acceleration or vertical speed.

Keep the data graphic, data text, and data ticks on the same stream and conversion.

Changing the source or active timeline range can change a telemetry-derived scale. Preview and rebuild range-dependent graphics where required before export.

## Configure major and minor ticks

Choose how major ticks are generated:

- Step mode places major ticks at a selected value interval.
- Count mode divides the range into a selected number of equal intervals.

Then set:

- Major step or interval count
- Minor ticks per major interval
- Whether to include an exact maximum tick
- Major and minor tick lengths
- Major and minor stroke widths
- Tick offset and line cap

Use stronger major marks and lighter minor marks to preserve hierarchy. Too many minor ticks can become a solid band after the template is scaled down.

## Style the guide line and labels

Show or hide the guide line, then choose its color, stroke width, and line cap.

For labels, configure:

- Visibility and label frequency
- Font, size, weight, fill, and outline
- Decimal places
- Prefix and suffix
- Trimming of trailing zeroes

Label every second or third major tick when every label would overlap. Use a suffix such as "mph" only when the tick labels and mapped graphic use that unit.

## Align ticks with the gauge

Select the tick layer and gauge together, then use center alignment where appropriate. For radial designs, enter identical center coordinates when exact alignment is required.

Check:

- Minimum and maximum positions
- Direction of increase
- Needle or progress alignment at zero and maximum
- Label clearance
- Stroke visibility at final export size

Preview several telemetry values rather than only the first frame.

## Save the template

Use "Template" > "Save As New" for an edited built-in design or "Save" for an existing custom template.

The completed scale now uses linear or radial ticks whose geometry, labels, units, and range agree with the telemetry graphic.
