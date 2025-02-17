# Visual Refinements

Like any other design project, Encode Sans has been evolved and refined over time. As good as the current version is, there are a few opportunities to make it just a little more harmonious of a design. 

Jacques Le Bailly (@fonthausen) is in NYC this week, so I took the opportunity to consult with him about a few possible changes. It was a great opportunity to understand the logic behind some of the design decisions, and to quick sketch ideas together for improvements.

## Uppercase German Double S (ẞ, Unicode 1E9E)

As of October, 2016, the `/Germandbls` had a form that was relatively unique for this glyph. I asked a couple of German friends in type design, and they agreed that it looked out-of-place. 

![Original Germandbls in Encode Sans](assets/2018-11-01-15-29-59.png).

Talking with Jacques, he expressed that it should keep some of the top curvature present in letters of Encode Sans, like `/B` and `/R`. 

My first effort wasn't quite feeling right ... it was maybe a little overly-sharp at the top.

![](assets/2018-11-01-15-49-15.png)

I looked for further design guidance in sources such as the [Proposal to encode Latin Capital Letter Sharp S to the UCS](http://std.dkuug.dk/jtc1/sc2/wg2/docs/n3227.pdf), a [Medium article from Christoph Koeberlin](https://medium.com/@typefacts/the-german-capital-letter-eszett-e0936c1388f8), and [design suggestions from Ralf Herrmann](https://typography.guru/journal/capital-sharp-s-designs/).


I started to see that I could keep the left part of Encode's original `/Germandbls`  so as to not make it overly-blocky. I could also borrow the top right corner of the `/Z` to make sure it followed the overall construction logic of the typeface. I feel that this form is fitting in quite well. It still needs a bit more tweaking to feel really finalized, but I like how it's looking:

![New Germandbls in Encode Sans](assets/2018-11-01-15-30-56.png)

![New Germandbls in Encode Sans](assets/2018-11-01-15-30-19.png)

![New Germandbls in Encode Sans](assets/2018-11-01-15-31-08.png)

![New Germandbls in Encode Sans](assets/2018-11-01-15-31-24.png)

![New Germandbls in Encode Sans, across styles](assets/Germandbls.gif)

I've used [RMX Tools](https://remix-tools.com) to convert these into small caps, as well.

Later, I did a second round to combine the separate contours (keeping inner corners open), and refine the curves. I paid special attention to matching the smoothness and subtle bounce of glyphs like `/three /five /R /B`.

![](assets/SS-narrow_light.png)
![](assets/SS-wide_light.png)
![](assets/SS-narrow_bold.png)
![](assets/SS-wide_bold.png)


## Fixing the thin `/Enj.sc`

The `/Enj.sc` had a couple of interpolation errors, which were simple to fix.

![](assets/Enj-narrow.png)
![](assets/Enj-wide.png)

Fixed: 

![](assets/Enj-narrow-fixed.png)
![](assets/Enj-wide-fixed.png)

## Making ogoneks connect a bit more smoothly

The ogonek doesn't connect with the bottom-right of the `/E` as well as it should. It also creates an odd little "kink" in the `/a` and `/u`.

![](assets/2018-11-01-17-27-53.png)

![](assets/2018-11-01-17-28-07.png)

The `/Eogonek` was easily fixed by moving the `ogonek` anchor to the corner. The `/aogonek` and `/uogonek` were resolved by decomposing the base letters, then moving their points down into the ogonek slightly. 

![](assets/2018-11-01-17-31-08.png)

![](assets/2018-11-01-17-31-17.png)

## Making diagonal accents match the sharpness of other diagonals in typeface

Encode Sans has a sharp and precise aesthetic, with (almost) all terminals and diagonals ending in vertical or horizontal terminations, in letters (like `/a /c /e /s`) and in other marks (like `/slash /fraction`). This links it to classic humanist typefaces like Gill Sans, Frutiger, and Verdana. However, the diagonal accents in letters like `/Oslash` and `/lslash` end in angled, "square capped" terminals.

Potentially, a few other diagonals might be better with sharp terminals, as well. Likely arrows. I'm less certain about math symbols like `/notequal`, as `/multiply` obviously shouldn't have flat terminals.

![](assets/2018-11-01-18-13-57.png)

Jacques tried to change it quickly, and showed that in order to change this well, it will be necessary to also consider changing the angle of these strokes.

**`/Lslash` and `/lslash`**

For the `/Lslash` and `/lslash`, I kept the angle of the slash and kept the overall location of the slash on the `L`s. 

![](assets/lslash-narrow_light.png)
![](assets/lslash-wide_light.png)
![](assets/lslash-narrow_bold.png)
![](assets/lslash-wide_bold.png)

**`/Oslash`, `/Oslash.sc`, and `/oslash`**

![](assets/oslash-nl.png)
![](assets/oslash-wl.png)
![](assets/oslash-nb.png)
![](assets/oslash-wb.png)

For a few of the more difficult slashes (especially in the `/oslash`, which has a more-complex structure), I made use of GlyphsApp's ability to place guides against two selected points, with the midpoint marked. This kept the slashes centered against the `o`s, and allowed control of the terminal locations.

![](assets/oslash-guides.gif)

## Still to be completed

- [x] `/Germandbls`: check kerning, probably add against `/W /Y /V` and punctuation
- [x] fix diagonal accent terminals
- [x] double-check kerning in slash accents

## Kerning `/Germandbls`

I've kerned the new cap and smallcap `/Germandbls` across all 4 masters. It is in the `/S` kern1 group (they share kerns on their right sides, or the "first" side of letter gaps), which made it a bit faster (and also meant that `/S` got an update against the `/A`).

![](assets/2019-01-02-16-40-05.png)

![](assets/2019-01-02-16-41-47.png)

![](assets/2019-01-02-16-44-25.png)

## Kerning new slashes

I made only a few small adjustments to existing slash kerns, where the flat ends cause gaps to appear unequal (for instance, in `XXØXX` where letters crash unequally)

![](assets/2019-01-02-16-51-10.png)

![](assets/2019-01-02-16-52-22.png)

Meanwhile, I think the lowercase kerning already works well in almost all cases – probably partly because there are so many fewer crashes. I have modified it slightly for condensed bold diagonals, and nowhere else.

![](assets/2019-01-02-16-57-53.png)
