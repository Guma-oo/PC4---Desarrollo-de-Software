async function loadPets(sortBy = "") {
    let url = "http://localhost:8000/pets/";
    if (sortBy) url += `?sort_by=${sortBy}`;
    
    const res = await fetch(url);
    const pets = await res.json();
    const list = document.getElementById("petList");
    list.innerHTML = "";
    
    pets.forEach(p => {
        let badgeColor = p.status === "Perdida" ? "bg-danger" : p.status === "En Resguardo" ? "bg-warning text-dark" : "bg-success";
        
        list.innerHTML += `
            <li class="list-group-item">
                <strong>${p.name}</strong> (${p.species} - ${p.breed}) 
                <span class="badge ${badgeColor}">${p.status}</span>
                <br><small> ${p.location} | ${p.description}</small>
                <br>
                <button onclick="advanceStatus(${p.id})" class="btn btn-sm btn-outline-secondary mt-2">Avanzar Estado</button>
            </li>`;
    });
}

async function advanceStatus(petId) {
    await fetch(`http://localhost:8000/pets/${petId}/advance-status`, { method: 'PUT' });
    loadPets(); // Recarga la lista
}

document.getElementById("petForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = {
        name: document.getElementById("name").value,
        species: document.getElementById("species").value,
        breed: document.getElementById("breed").value,
        location: document.getElementById("location").value,
        description: document.getElementById("description").value
    };
    await fetch("http://localhost:8000/pets/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    e.target.reset();
    loadPets();
});

loadPets();