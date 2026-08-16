# How to Fit Telemetry Data Minimum and Maximum Values to a Gauge

The "fit data min/max" mapping adapts a numeric graphic to the lowest and highest values in the active telemetry data. It is useful when a gauge should use its complete visual range for one source or selected segment without manually entering input limits.

Because the scale is source-dependent, the same value can appear at a different position when another clip or timeline range is loaded.

## Understand min/max fitting

The mapping takes:

- The lowest value in the relevant active data
- The highest value in the relevant active data

It maps those endpoints to the output range expected by the graphic. Intermediate values are placed proportionally between them.

For example, a clip ranging from 10 to 30 can fill the same gauge travel as another ranging from 40 to 80. The visual position represents progress through that source's range, not a universal fixed scale.

## 1. Load the source and gauge

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Load the intended GoPro telemetry and open a template containing a numeric data graphic, or add a compatible data-graphic layer.

Use "Template" > "Save As New" when modifying a built-in template.

## 2. Map the telemetry stream

Select the gauge layer and open its data or input controls.

1. Choose "Stream."
2. Select the required numeric stream.
3. Choose the intended unit with "Convert."
4. Confirm that the gauge responds while scrubbing the timeline.

The conversion should be final before evaluating the input range.

## 3. Select fit data min/max

Open "Map / normalize input" and choose "fit data min/max."

The graphic now uses the active data minimum and maximum rather than explicit input boundaries. Keep the configured output range appropriate to the graphic, such as the full travel of a bar, pointer, fill, or arc.

If the layer shows little movement, verify that the stream actually varies during the active data.

## 4. Coordinate the ticks

If the gauge has data ticks:

1. Map them to the same stream.
2. Apply the same conversion.
3. Set "Bounds source" to use the stream.
4. Add minimum or maximum padding when labels need space beyond the extremes.
5. Use "Nice scale" if rounded tick boundaries are easier to read.

Static ticks with unrelated limits can make an automatically fitted gauge misleading. Replace them with data ticks or update them to match the fitted range.

## 5. Decide whether zero belongs on the scale

Automatic min/max fitting does not necessarily include zero. A stream whose values remain between 35 and 50 can use that interval as the complete gauge.

Enable "Include zero" on compatible data ticks when the scale must show its relationship to zero. For a graphic, choose a fixed or symmetric map instead when zero must occupy a specific visual position.

Do not use ordinary min/max fitting for a signed indicator that requires zero at the center. Use "fit max absolute" for that purpose.

## 6. Set the final timeline range

The active segment can determine the minimum and maximum.

1. Set the final in point.
2. Set the final out point.
3. Select "Rebuild data graphics from range."
4. Wait for the gauge and range-dependent data to update.
5. Review the new endpoints and movement.

Removing a high or low event from the segment can change the complete scale. Rebuild before finalizing tick labels, padding, and layout.

## 7. Handle an isolated spike

One unusual sample can become the automatic maximum or minimum and compress the rest of the gauge movement.

Before limiting it:

- Compare the value with surrounding frames.
- Check related speed, altitude, GPS, or motion behavior.
- Decide whether the sample is plausible.

If it should not dominate the visual scale, use "Clamp values" on the layer input. Clamping occurs before range mapping, so the fitted endpoints use the limited data. Clamping does not repair the source telemetry.

## 8. Preview the complete range

Inspect:

- The minimum frame
- The maximum frame
- Several middle values
- A quiet or stationary section
- The final selected range

Confirm that the gauge reaches the expected endpoints and the numeric readout agrees. A stream with an extremely narrow range can fill the gauge even though the actual change is small, so include labels or ticks that communicate the values.

## 9. Know when to use another method

Use "fixed range" when:

- Several clips must be compared directly.
- A gauge has a known physical or editorial scale.
- Zero must remain at a fixed position.
- The scale should not change when the timeline range changes.

Use "fit max absolute" when positive and negative values should share equal limits around zero.

## 10. Save the adaptive gauge

Save the custom template after the active range, data ticks, labels, and spike handling are correct.

The gauge now adapts its complete visual travel to the telemetry minimum and maximum found in the intended source or selected segment.
