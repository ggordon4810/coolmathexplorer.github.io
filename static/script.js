ocument.addEventListener("DOMContentLoaded", () => {
    initializeNavigation();
    markCurrentNavigationLink();
    initializeCollatzChart();
    initializeTriangleVisual();
});


function initializeNavigation() {
    const toggle = document.querySelector(".nav-toggle");
    const links = document.querySelector("#nav-links");

    if (!toggle || !links) {
        return;
    }

    toggle.addEventListener("click", () => {
        const isOpen = links.classList.toggle("open");

        toggle.setAttribute(
            "aria-expanded",
            String(isOpen)
        );
    });

    links.addEventListener("click", (event) => {
        if (event.target.matches("a")) {
            links.classList.remove("open");
            toggle.setAttribute("aria-expanded", "false");
        }
    });
}


function markCurrentNavigationLink() {
    const currentPath =
        window.location.pathname.replace(/\/$/, "") || "/";

    const navigationLinks =
        document.querySelectorAll(".nav-links a");

    navigationLinks.forEach((link) => {
        const linkPath =
            new URL(link.href).pathname.replace(/\/$/, "") || "/";

        if (linkPath === currentPath) {
            link.classList.add("active");
            link.setAttribute("aria-current", "page");
        }
    });
}


function initializeCollatzChart() {
    const canvas = document.querySelector("#collatz-chart");

    if (!canvas || typeof Chart === "undefined") {
        return;
    }

    let sequence;

    try {
        sequence = JSON.parse(canvas.dataset.sequence);
    } catch (error) {
        console.error(
            "The Collatz sequence could not be read.",
            error
        );

        return;
    }

    if (!Array.isArray(sequence) || sequence.length === 0) {
        return;
    }

    const labels = sequence.map(
        (_, index) => `Step ${index}`
    );

    const pointColors = sequence.map((value) => {
        if (value % 2 === 0) {
            return "#6557e8";
        }

        return "#17a5a5";
    });

    new Chart(canvas, {
        type: "line",

        data: {
            labels: labels,

            datasets: [
                {
                    label: "Collatz value",
                    data: sequence,
                    borderColor: "#6557e8",
                    backgroundColor: "rgba(101, 87, 232, 0.12)",
                    pointBackgroundColor: pointColors,
                    pointBorderColor: pointColors,
                    pointRadius: sequence.length > 60 ? 2 : 4,
                    pointHoverRadius: 6,
                    borderWidth: 2.5,
                    fill: true,
                    tension: 0.18
                }
            ]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            interaction: {
                intersect: false,
                mode: "index"
            },

            plugins: {
                legend: {
                    display: false
                },

                tooltip: {
                    callbacks: {
                        label(context) {
                            const value =
                                Number(context.raw).toLocaleString();

                            return `Value: ${value}`;
                        }
                    }
                }
            },

            scales: {
                x: {
                    title: {
                        display: true,
                        text: "Step"
                    },

                    grid: {
                        display: false
                    }
                },

                y: {
                    beginAtZero: true,

                    title: {
                        display: true,
                        text: "Value"
                    },

                    ticks: {
                        callback(value) {
                            return Number(value).toLocaleString();
                        }
                    }
                }
            }
        }
    });
}


function initializeTriangleVisual() {
    const container =
        document.querySelector(".triangle-visual");

    if (!container) {
        return;
    }

    const position = Number.parseInt(
        container.dataset.position,
        10
    );

    if (!Number.isInteger(position) || position < 1) {
        return;
    }

    const maximumRows = 20;
    const rowsToDisplay = Math.min(
        position,
        maximumRows
    );

    for (
        let rowNumber = 1;
        rowNumber <= rowsToDisplay;
        rowNumber += 1
    ) {
        const row = document.createElement("div");

        row.className = "triangle-row";

        for (
            let dotNumber = 0;
            dotNumber < rowNumber;
            dotNumber += 1
        ) {
            const dot = document.createElement("span");

            dot.className = "triangle-dot";
            row.appendChild(dot);
        }

        container.appendChild(row);
    }

    if (position > maximumRows) {
        const note = document.createElement("p");

        note.className = "triangle-limit-note";
        note.textContent =
            `Showing the first ${maximumRows} of ${position} rows.`;

        container.appendChild(note);
    }
}

