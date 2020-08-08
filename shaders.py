from gl import *

def gourad(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )
    #print(intensity)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )
    #print(intensity)
    if (intensity>=0 and intensity<0.3):
        intensity=0
    elif (intensity>=0.3 and intensity<0.5):
        intensity=0.3
    elif (intensity>=0.5 and intensity<0.8):
        intensity=0.5
    elif (intensity>=0.8 and intensity<=1):
        intensity=0.8

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0