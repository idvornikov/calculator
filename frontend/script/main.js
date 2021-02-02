async function loadData(url, method = 'GET', data = null) {
    let requestData = {method: 'GET'};
    if (method === 'POST') {
        requestData = {
            method: 'POST',
            body: data
        }
    }
    let response = await fetch(url, requestData);
    return await response.json()
}


async function addStateCodeOptions(codes) {
    let state_code_select = window.document.getElementById('state_code');
    Object.values(codes).forEach(
        value => state_code_select.options[state_code_select.options.length] = new Option(value, value)
    );
}

loadData('http://localhost:8000/api/v1/calculator/state_code/').then(addStateCodeOptions)

function addCalculatedData(data) {
    let rawOrderCost = window.document.getElementById('rawOrderCost');
    let discount = window.document.getElementById('discount');
    let orderWithDiscount = window.document.getElementById('orderWithDiscount');
    let taxes = window.document.getElementById('taxes');
    let finalOrderCost = window.document.getElementById('finalOrderCost');
    rawOrderCost.textContent = data.raw_order_cost;
    discount.textContent = data.discount;
    orderWithDiscount.textContent = data.order_with_discount;
    taxes.textContent = data.taxes;
    finalOrderCost.textContent = data.final_order_cost;
}

let formElem = window.document.getElementById('formElem');
formElem.onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData(formElem);
    let data = {};
    formData.forEach((value, key) => data[key] = value);
    let json = JSON.stringify(data);
    loadData('http://localhost:8000/api/v1/calculator/', 'POST', json).then(addCalculatedData)
};
