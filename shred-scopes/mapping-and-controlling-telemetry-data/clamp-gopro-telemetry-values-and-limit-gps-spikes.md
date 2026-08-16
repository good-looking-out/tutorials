# How to Clamp GoPro Telemetry Values and Limit GPS Spikes

"Clamp values" limits a numeric layer input to an entered minimum and maximum. A value below the minimum becomes the minimum, and a value above the maximum becomes the maximum for that layer.

Clamping can keep an unusual GPS or sensor sample from pushing a gauge outside its operating range or dominating automatic range fitting. It does not correct or delete the extracted telemetry.

## When clamping is appropriate

Consider clamping when:

- One implausible speed sample compresses the useful gauge movement.
- An altitude spike stretches a profile or scale.
- A signed G or acceleration indicator leaves its intended bounds.
- A graphic must remain within a known editorial range.
- Automatic min/max mapping is dominated by an isolated extreme.

Do not use clamping merely to make valid high or low events appear less significant. Review the source and surrounding telemetry before selecting limits.

## 1. Open the mapped layer

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load the intended telemetry.

Open the template, select the numeric data-text, data-graphic, or data-ticks layer, and expand its input controls.

Create a custom copy before changing a built-in template.

## 2. Confirm the stream and unit

Choose the intended "Stream" and "Convert" setting first.

Clamping uses the converted unit. If speed is converted to mph, clamp values are entered in mph. If altitude is converted to feet, its limits are in feet.

Changing the conversion later requires recalculating the clamp limits.

## 3. Enable Clamp values

Open "Input advanced" and enable "Clamp values." Enter:

- "Clamp min" for the lowest value the layer may receive
- "Clamp max" for the highest value the layer may receive

Choose limits based on the activity, intended graphic, and reviewed data. For a speedometer that should never display a negative value, a minimum of zero can be appropriate. The maximum should still allow valid high-speed events.

## 4. Understand the processing order

The relevant order is:

1. Unit conversion
2. Input clamping
3. Deadband
4. Range mapping

This means an automatic min/max map sees the clamped values rather than the original extremes for that layer.

Another layer mapped to the same stream remains unchanged unless it has its own clamp settings.

## 5. Distinguish input and output clamping

"Clamp values" limits incoming telemetry before mapping.

"Clamp mapped output" is a separate option for fixed-range maps. It limits the result produced by the mapping so the graphic does not travel beyond its output interval.

Use input clamping when the layer should treat all source values beyond a boundary as that boundary. Use mapped-output clamping when the input value may remain meaningful but the visual result must stay within the graphic's travel.

## 6. Preview the suspected spike

Scrub to the unusual event and compare:

- The frame before it
- The extreme frame
- The frame after it
- Related telemetry streams
- Visible action in Source Composite when source video is available

An abrupt isolated value is more likely to be unsuitable for the scale than a sustained high value that agrees with the footage and related streams.

Do not describe a clamped display as repaired telemetry. The layer is showing a limited representation.

## 7. Coordinate related layers

A gauge, data text, and ticks can each have separate input settings. Decide whether all should show the same limited value.

For consistency:

- Apply the same conversion.
- Apply the same clamp limits where appropriate.
- Use a compatible map and tick range.
- Check running maximum or minimum layers separately.

A numeric text layer without the clamp can reveal the original extreme while a clamped gauge stops at its maximum. That can be intentional, but it should not appear accidental.

## 8. Combine clamping with smoothing carefully

Smoothing averages changes over time, while clamping imposes hard boundaries. Smoothing can reduce short spikes without creating a flat maximum, but it can also soften real short events.

For grade, use its purpose-built smoothing and adaptive controls before relying only on a hard clamp. For speed, altitude, or G-force, compare both approaches against the full timeline.

## 9. Test the boundaries

Preview values:

- Below the minimum
- At the minimum
- Inside the range
- At the maximum
- Above the maximum

Confirm that the text, graphic, and ticks behave as intended and that no important valid event is flattened.

If automatic mapping still appears compressed, verify that the data graphics were rebuilt for the final timeline range after the clamp was configured.

## 10. Save and disclose through labeling

Save the custom template after testing. Use neutral labels that identify the measurement and unit without implying altered source accuracy.

The selected layer now stays within its intended input limits while the underlying extracted telemetry remains unchanged for other layers and future mappings.
