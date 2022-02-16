function createSlideUI(slide, placement) {
    /*********************************************************************
     * Create a new <div> element which contains all the slide information.
     * Store a reference to the created DOM node so we can use it to place
     * other DOM nodes and connect events.
     *********************************************************************/
    const slideElement = document.createElement("div");
    // Assign the ID of the slide to the <span> element
    slideElement.id = slide.id;
    slideElement.classList.add("slide");

    /*********************************************************************
     * Place the newly created DOM node cat the beginning of the slidesDiv
     *********************************************************************/
    const slidesDiv = document.getElementById("slidesDiv");
    if (placement === "first") {
    slidesDiv.insertBefore(slideElement, slidesDiv.firstChild);
    } else {
    slidesDiv.appendChild(slideElement);
    }

    /*********************************************************************
     * Create a <div> element to contain the slide title text
     *********************************************************************/
    const title = document.createElement("div");
    title.innerText = slide.title.text;
    // Place the title of the slide in the <div> element
    slideElement.appendChild(title);

    /*********************************************************************
     * Create a new <img> element and place it inside the newly created slide
     * element. This will reference the thumbnail from the slide.
     *********************************************************************/
    const img = new Image();
    // Set the src URL of the image to the thumbnail URL of the slide
    img.src = slide.thumbnail.url;
    // Set the title property of the image to the title of the slide
    img.title = slide.title.text;
    // Place the image inside the new <div> element
    slideElement.appendChild(img);

    /*********************************************************************
     * Set up a click event handler on the newly created slide. When clicked,
     * the code defined below will execute.
     *********************************************************************/
    slideElement.addEventListener("click", () => {
    /*******************************************************************
     * Remove the "active" class from all elements with the .slide class
     *******************************************************************/
    const slides = document.querySelectorAll(".slide");
    Array.from(slides).forEach((node) => {
        node.classList.remove("active");
    });

    /*******************************************************************
     * Add the "active" class on the current element being selected
     *******************************************************************/
    slideElement.classList.add("active");

    /******************************************************************
     * Applies a slide's settings to the SceneView.
     *
     * Each slide has a viewpoint and visibleLayers property that define
     * the point of view or camera for the slide and the layers that should
     * be visible to the user when the slide is selected. This method
     * allows the user to animate to the given slide's viewpoint and turn
     * on its visible layers and basemap layers in the view.
     ******************************************************************/
     slide.applyTo(view);
    });
}
