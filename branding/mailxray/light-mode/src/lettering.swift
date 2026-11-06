import Foundation
import CoreText
import CoreGraphics

func number(_ value: CGFloat) -> String { String(format: "%.3f", Double(value)) }
func outline(_ text: String, fontName: String) -> [String: Any] {
    let font = CTFontCreateWithName(fontName as CFString, 100, nil)
    let line = CTLineCreateWithAttributedString(NSAttributedString(string: text, attributes: [NSAttributedString.Key(kCTFontAttributeName as String): font]))
    var data = ""
    for run in CTLineGetGlyphRuns(line) as! [CTRun] {
        let count = CTRunGetGlyphCount(run)
        var glyphs = [CGGlyph](repeating: 0, count: count)
        var positions = [CGPoint](repeating: .zero, count: count)
        CTRunGetGlyphs(run, CFRange(location: 0, length: 0), &glyphs)
        CTRunGetPositions(run, CFRange(location: 0, length: 0), &positions)
        for i in 0..<count {
            guard let path = CTFontCreatePathForGlyph(font, glyphs[i], nil) else { continue }
            func point(_ p: CGPoint) -> String { "\(number(p.x + positions[i].x)),\(number(-p.y))" }
            path.applyWithBlock { pointer in
                let e = pointer.pointee
                switch e.type {
                case .moveToPoint: data += "M" + point(e.points[0])
                case .addLineToPoint: data += "L" + point(e.points[0])
                case .addQuadCurveToPoint: data += "Q" + point(e.points[0]) + " " + point(e.points[1])
                case .addCurveToPoint: data += "C" + point(e.points[0]) + " " + point(e.points[1]) + " " + point(e.points[2])
                case .closeSubpath: data += "Z"
                @unknown default: break
                }
            }
        }
    }
    return ["path": data, "width": CTLineGetTypographicBounds(line, nil, nil, nil)]
}
var result: [String: Any] = [:]
for text in ["Mail", "Xray"] { result[text] = outline(text, fontName: "ArialRoundedMTBold") }
for text in ["by ", "Spam", "Scope"] { result[text] = outline(text, fontName: "AvenirNext-Regular") }
let json = try JSONSerialization.data(withJSONObject: result, options: [.sortedKeys])
try json.write(to: URL(fileURLWithPath: CommandLine.arguments[1]))
