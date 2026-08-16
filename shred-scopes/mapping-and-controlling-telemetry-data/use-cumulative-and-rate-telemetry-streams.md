# How to Use Cumulative and Rate Telemetry Streams

Cumulative streams total activity through the current frame, while rate streams measure how quickly a supported value changes per second. Shred Scopes can use these derived values for distance, airtime, elevation gain or loss, elapsed duration, and rate-of-change displays.

The active source must contain the measurements required to derive each stream.

## Understand cumulative values

Available cumulative or progressive values include:

- "Distance traveled," which totals distance along valid GPS positions
- "Cumulative airtime," which totals detected in-air event duration
- "Cumulative altitude gain," which totals positive altitude changes
- "Cumulative altitude loss," which totals the magnitude of negative altitude changes
- "Elapsed time," which measures progress from the active start

These values normally increase or remain stable as the timeline advances. They do not decrease when the source reverses direction or descends unless a different non-cumulative stream is selected.

## Understand rate variants

A rate stream measures how quickly a supported source value changes each second.

Its default unit is the source unit per second. Examples include:

- A speed-rate variant expressed as speed change per second
- An altitude-rate variant expressed in m/s

Conversions appear only when the resulting rate matches a supported unit. Altitude rate provides compatible m/s conversions; many other rate variants have no additional conversion.

Use a rate variant only when it appears for the active source and its meaning matches the intended label.

## 1. Load the telemetry

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load the intended source.

Open a template or create a custom one. Inspect "Stream" on a data layer to see which cumulative and rate variants are available.

## 2. Add a cumulative data-text layer

1. Add "data·text."
2. Select the required cumulative stream.
3. Choose the unit conversion where available.
4. Configure decimal places or duration formatting.
5. Add a clear static label.

For distance and altitude gain or loss, choose feet, yards, miles, kilometers, or the default meters as appropriate. For cumulative airtime and elapsed time, use raw seconds or a compatible duration format.

## 3. Distinguish altitude gain and loss

"Cumulative altitude gain" adds only positive altitude changes. "Cumulative altitude loss" adds the magnitude of negative changes.

Both totals are positive cumulative distances. The loss total should not be given a negative sign merely because it represents descending movement.

Use separate labels such as "ASCENT" and "DESCENT" when displaying both.

## 4. Add a rate layer

1. Add or select a data-text or compatible data-graphic layer.
2. Open "Stream."
3. Choose the rate variant of the intended base stream.
4. Apply a conversion only when one is offered and appropriate.
5. Label the result with its complete rate unit.

A source unit and its rate are different measurements. Speed describes motion; rate of speed describes how quickly that speed changes. Altitude describes elevation; altitude rate describes how quickly elevation changes.

## 5. Set signed ranges for rate

Rate values can be positive or negative. Use:

- "fit max absolute" for an adaptive scale centered on zero
- A symmetric "fixed range" for a consistent scale

Confirm the sign's meaning for the chosen base stream. Add a deadband around zero when small changes make the indicator jitter, and use smoothing cautiously when short events must remain visible.

## 6. Reset cumulative values for a segment

To make totals begin at the selected in point:

1. Set the final in point.
2. Set the final out point.
3. Choose "Rebuild data graphics from range."
4. Confirm that distance, cumulative airtime, elevation gain or loss, and elapsed time begin at 0 where applicable.
5. Review the final totals at the out point.

Without rebuilding, cumulative values can include activity before the intended export segment.

## 7. Recalculate rate and range behavior

Rebuilding also recalculates range-relative streams and automatic mappings for the selected segment. A strong event outside the new range should no longer determine an adaptive rate scale.

Choose the final range before setting automatic ticks or interpreting the maximum visible rate.

## 8. Coordinate current, cumulative, and rate displays

A combined design can show:

- Current speed, distance traveled, and rate of speed change
- Current altitude, cumulative gain, cumulative loss, and altitude rate
- In-air state and cumulative airtime

Use distinct labels and units. Do not present a cumulative total as a current value or a rate as a total.

Apply the same source and selected range across related layers.

## 9. Preview for resets and unexpected jumps

Inspect:

- The first frame of the active range
- A period when the cumulative value should remain stable
- A period when it should increase
- Positive and negative rate events
- The final cumulative total

GPS gaps or altitude noise can affect derived distance, gain, loss, and rate values. Smoothing or clamping changes only the selected presentation and should not be described as repairing the source.

## 10. Save the derived-data template

Save the custom template after verifying the active range, units, labels, signed interpretation, and final totals.

The overlay now uses cumulative streams to summarize activity through the current frame and rate streams to show how quickly supported measurements are changing.
