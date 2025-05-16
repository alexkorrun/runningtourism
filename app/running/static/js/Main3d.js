const section = document.getElementById("hero"),
      image = section.querySelector(".hero-image");

section.addEventListener("mousemove", (e) => {
    const { width, height, left, top } = section.getBoundingClientRect(),
           x = e.clientX - left - width / 3,
           y = e.clientY - top - height / 3;

    const rotateX = (y / height) * -5,
          rotateY = (x / width) * 5;
          
    image.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.03)`;
});

section.addEventListener("mouseleave", () => {
    image.style.transform = "rotateX(0deg) rotateY(0deg) scale(1)";
});