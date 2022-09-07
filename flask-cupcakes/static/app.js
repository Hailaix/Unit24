const $cupcakes = $('#cupcakes')
const $cupcakeForm = $('#cupcake-form')

const BASE_URL = "/api/cupcakes"

function createCupcakeLI(cupcake) {
    return $(`
    <li data-id="${cupcake.id}">
        <img src="${cupcake.image}" style="max-height:10rem;">
        This ${cupcake.size} cupcake is ${cupcake.flavor} flavor, rated ${cupcake.rating}
    </li>
    `);
}

async function listCupcakes() {
    const res = await axios({
        url: BASE_URL,
        method: "GET"
    })
    $cupcakes.empty()
    for(let cupcake of res.data.cupcakes){
        $cupcakes.append(createCupcakeLI(cupcake))
    }
}

$cupcakeForm.on("submit", async function(e){
    e.preventDefault();
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const image = $("#image").val();
    
    const res = await axios({
        url: BASE_URL,
        method: "POST",
        data: {
            flavor,
            size,
            rating,
            image
        }
    });
    const cupcake = res.data.cupcake;
    $cupcakes.append(createCupcakeLI(cupcake));
})

$(listCupcakes);