def voronoi_otsu_labeling(image, spot_sigma: float = 2, outline_sigma: float = 2):
    """Voronoi-Otsu-Labeling is a segmentation algorithm for blob-like structures such as nuclei and
    granules with high signal intensity on low-intensity background.

    The two sigma parameters allow tuning the segmentation result. The first sigma controls how close detected cells
    can be (spot_sigma) and the second controls how precise segmented objects are outlined (outline_sigma). Under the
    hood, this filter applies two Gaussian blurs, spot detection, Otsu-thresholding and Voronoi-labeling. The
    thresholded binary image is flooded using the Voronoi approach starting from the found local maxima. Noise-removal
    sigma for spot detection and thresholding can be configured separately.

    This allows segmenting connected objects such as not to dense nuclei.
    If the nuclei are too dense, consider using stardist [1] or cellpose [2].

    See also
    --------
    .. [0] https://github.com/clEsperanto/pyclesperanto_prototype/blob/master/demo/segmentation/voronoi_otsu_labeling.ipynb
    .. [1] https://www.napari-hub.org/plugins/stardist-napari
    .. [2] https://www.napari-hub.org/plugins/cellpose-napari
    """
    import numpy as np
    from skimage.filters import threshold_otsu as sk_threshold_otsu, gaussian
    from skimage.segmentation import watershed
    from skimage.measure import label
    from skimage.morphology import local_maxima

    
    image = np.asarray(image)

    # blur and detect local maxima
    blurred_spots = gaussian(image, spot_sigma)
    spot_centroids = local_maxima(blurred_spots)

    # blur and threshold
    blurred_outline = gaussian(image, outline_sigma)
    threshold = sk_threshold_otsu(blurred_outline)
    binary_otsu = blurred_outline > threshold

    # determine local maxima within the thresholded area
    remaining_spots = spot_centroids * binary_otsu

    # start from remaining spots and flood binary image with labels
    labeled_spots = label(remaining_spots)
    labels = watershed(binary_otsu, labeled_spots, mask=binary_otsu)

    return labels


def local_minima_seeded_watershed(image, spot_sigma: float = 10, outline_sigma: float = 0):
    """
    Segment cells in images with fluorescently marked membranes.

    The two sigma parameters allow tuning the segmentation result. The first sigma controls how close detected cells
    can be (spot_sigma) and the second controls how precise segmented objects are outlined (outline_sigma). Under the
    hood, this filter applies two Gaussian blurs, local minima detection and a seeded watershed.

    See also
    --------
    .. [1] https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_watershed.html
    """
    import numpy as np
    from skimage.filters import gaussian
    from skimage.segmentation import watershed
    from skimage.measure import label
    from skimage.morphology import local_minima

    image = np.asarray(image)

    spot_blurred = gaussian(image, sigma=spot_sigma)

    spots = label(local_minima(spot_blurred))

    if outline_sigma == spot_sigma:
        outline_blurred = spot_blurred
    else:
        outline_blurred = gaussian(image, sigma=outline_sigma)

    return watershed(outline_blurred, spots)