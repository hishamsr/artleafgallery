from django.contrib import admin

from .models import Product, Category, ArtImage, Artist, Frame, Company

COLORS = [
# ("#f0f8ff", "aliceblue"),
# ("#faebd7", "antiquewhite"),
# ("#00ffff", "aqua"),
# ("#7fffd4", "aquamarine"),
# ("#f0ffff", "azure"),
# ("#f5f5dc", "beige"),
# ("#ffe4c4", "bisque"),
# ("#000000", "black"),
# ("#ffebcd", "blanchedalmond"),
# ("#0000ff", "blue"),
# ("#8a2be2", "blueviolet"),
# ("#a52a2a", "brown"),
# ("#deb887", "burlywood"),
# ("#5f9ea0", "cadetblue"),
# ("#7fff00", "chartreuse"),
# ("#d2691e", "chocolate"),
# ("#ff7f50", "coral"),
# ("#6495ed", "cornflowerblue"),
# ("#fff8dc", "cornsilk"),
# ("#dc143c", "crimson"),
# ("#00ffff", "cyan"),
# ("#00008b", "darkblue"),
# ("#008b8b", "darkcyan"),
# ("#b8860b", "darkgoldenrod"),
# ("#a9a9a9", "darkgray"),
# ("#006400", "darkgreen"),
# ("#a9a9a9", "darkgrey"),
# ("#bdb76b", "darkkhaki"),
# ("#8b008b", "darkmagenta"),
# ("#556b2f", "darkolivegreen"),
# ("#ff8c00", "darkorange"),
# ("#9932cc", "darkorchid"),
# ("#8b0000", "darkred"),
# ("#e9967a", "darksalmon"),
# ("#8fbc8f", "darkseagreen"),
# ("#483d8b", "darkslateblue"),
# ("#2f4f4f", "darkslategray"),
# ("#2f4f4f", "darkslategrey"),
# ("#00ced1", "darkturquoise"),
# ("#9400d3", "darkviolet"),
# ("#ff1493", "deeppink"),
# ("#00bfff", "deepskyblue"),
# ("#696969", "dimgray"),
# ("#696969", "dimgrey"),
("#1e90ff", "dodgerblue"),
# ("#b22222", "firebrick"),
# ("#fffaf0", "floralwhite"),
# ("#228b22", "forestgreen"),
# ("#ff00ff", "fuchsia"),
# ("#dcdcdc", "gainsboro"),
# ("#f8f8ff", "ghostwhite"),
# ("#ffd700", "gold"),
# ("#daa520", "goldenrod"),
# ("#808080", "gray"),
# ("#008000", "green"),
# ("#adff2f", "greenyellow"),
# ("#808080", "grey"),
# ("#f0fff0", "honeydew"),
# ("#ff69b4", "hotpink"),
# ("#cd5c5c", "indianred"),
# ("#4b0082", "indigo"),
# ("#fffff0", "ivory"),
# ("#f0e68c", "khaki"),
# ("#e6e6fa", "lavender"),
# ("#fff0f5", "lavenderblush"),
# ("#7cfc00", "lawngreen"),
# ("#fffacd", "lemonchiffon"),
# ("#add8e6", "lightblue"),
# ("#f08080", "lightcoral"),
# ("#e0ffff", "lightcyan"),
# ("#fafad2", "lightgoldenrodyellow"),
# ("#d3d3d3", "lightgray"),
# ("#90ee90", "lightgreen"),
# ("#d3d3d3", "lightgrey"),
# ("#ffb6c1", "lightpink"),
# ("#ffa07a", "lightsalmon"),
# ("#20b2aa", "lightseagreen"),
# ("#87cefa", "lightskyblue"),
# ("#778899", "lightslategray"),
# ("#778899", "lightslategrey"),
# ("#b0c4de", "lightsteelblue"),
# ("#ffffe0", "lightyellow"),
# ("#00ff00", "lime"),
# ("#32cd32", "limegreen"),
# ("#faf0e6", "linen"),
# ("#ff00ff", "magenta"),
# ("#800000", "maroon"),
# ("#66cdaa", "mediumaquamarine"),
# ("#0000cd", "mediumblue"),
# ("#ba55d3", "mediumorchid"),
# ("#9370db", "mediumpurple"),
# ("#3cb371", "mediumseagreen"),
# ("#7b68ee", "mediumslateblue"),
# ("#00fa9a", "mediumspringgreen"),
# ("#48d1cc", "mediumturquoise"),
# ("#c71585", "mediumvioletred"),
# ("#191970", "midnightblue"),
# ("#f5fffa", "mintcream"),
# ("#ffe4e1", "mistyrose"),
# ("#ffe4b5", "moccasin"),
# ("#ffdead", "navajowhite"),
# ("#000080", "navy"),
# ("#fdf5e6", "oldlace"),
# ("#808000", "olive"),
# ("#6b8e23", "olivedrab"),
# ("#ffa500", "orange"),
# ("#ff4500", "orangered"),
# ("#da70d6", "orchid"),
# ("#eee8aa", "palegoldenrod"),
# ("#98fb98", "palegreen"),
# ("#afeeee", "paleturquoise"),
# ("#db7093", "palevioletred"),
# ("#ffefd5", "papayawhip"),
# ("#ffdab9", "peachpuff"),
# ("#cd853f", "peru"),
# ("#ffc0cb", "pink"),
# ("#dda0dd", "plum"),
# ("#b0e0e6", "powderblue"),
# ("#800080", "purple"),
# ("#663399", "rebeccapurple"),
("#ff0000", "red"),
# ("#bc8f8f", "rosybrown"),
# ("#4169e1", "royalblue"),
# ("#8b4513", "saddlebrown"),
# ("#fa8072", "salmon"),
# ("#f4a460", "sandybrown"),
# ("#2e8b57", "seagreen"),
# ("#fff5ee", "seashell"),
# ("#a0522d", "sienna"),
# ("#c0c0c0", "silver"),
("#87ceeb", "skyblue"),
# ("#6a5acd", "slateblue"),
# ("#708090", "slategray"),
# ("#708090", "slategrey"),
# ("#fffafa", "snow"),
# ("#00ff7f", "springgreen"),
# ("#4682b4", "steelblue"),
# ("#d2b48c", "tan"),
# ("#008080", "teal"),
# ("#d8bfd8", "thistle"),
# ("#ff6347", "tomato"),
("#40e0d0", "turquoise"),
# ("#ee82ee", "violet"),
# ("#f5deb3", "wheat"),
("#ffffff", "White"),
("#CECECE", "Very Light Grey"),
("#666666", "Dim Gray"),
("#9A6600", "Golden Brown"),
("#FE9901", "Orange Peel"),
("#FFCB99", "Peach Orange"),
("#CCFF00", "Electric Lime"),
("#01CC00", "Free Speech Green"),
("#6601FF", "Electric Indigo"),
("#CC00FF", "Electric Purple"),
("#FF0198", "Hollywood Cerise"),
# ("#f5f5f5", "whitesmoke"),
("#ffff00", "yellow"),
("#9acd32", "yellowgreen")
]

from django import forms



class ArtImageForm(forms.ModelForm):
    
    color = forms.ChoiceField(choices=COLORS)

class ArtImageAdmin(admin.ModelAdmin):
    form = ArtImageForm

admin.site.register(ArtImage, ArtImageAdmin)

class ArtImageInline(admin.TabularInline):
    form = ArtImageForm
    model = ArtImage
    extra = 0

class CatogoryInline(admin.TabularInline):
        model = Category
        extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ArtImageInline]

class ProductAdmin(admin.ModelAdmin):
    inlines = [CatogoryInline, ArtImageInline]

admin.site.register(Category, CategoryAdmin)

admin.site.register(Artist)
admin.site.register(Frame)
admin.site.register(Company)
admin.site.register(Product, ProductAdmin)