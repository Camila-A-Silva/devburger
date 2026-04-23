 async function mostrarCarrinho() {
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()

        const carrinho = document.querySelector(".cart__items")

        carrinho.innerHTML = "";

        let total = 0

        for (let dado of dados){
            
            total = total + dado.preco

            let linha = `<div class="cart__item" style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
      
                        <img src="${dado.imagem}" style="width: 60px; height: 60px; border-radius: 8px; object-fit: cover;">
                        
                        <div class="cart__item-info">
                            <p style="margin: 0; font-weight: bold;">🍔 ${dado.nome}</p>
                            <p style="margin: 0; color: #555;">R$ ${dado.preco}</p>
                        </div>

                        </div>`

            carrinho.innerHTML += linha
        }
        document.querySelector(".cart__total").textContent = "Total: R$ " + total
    };

};

mostrarCarrinho()