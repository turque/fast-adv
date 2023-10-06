function Cards() {
    return(
        <div className="provaCard">
            <div className="provaImg">
                <picture></picture>
            </div>

            <div className="row provaInfo">
                <h5>Nome da prova</h5>
                <p>data da prova</p>
                <button className="provaDetail">Visualizar</button>
            </div>
        </div>
    )
}

export default Cards