export async function inserirfuncionario(funcionario){
    const con=await conectar();
    const sql='insert into funcionarios(id,nome,cargo,salario)'
    'values(?,?,?,?)'
    const valores=[funcionario,id,funcionario,nome,funcionarios.cargo,
    funcionario.salario]
    const retorno=await con.query(sql,valores)
    return retorno[0]
}
export async function atualizarfuncionario(funcionario){
    const con=await conectar();
    const sql='update funcionarios set nome=?,cargo=?,salario=?'
    'where id=?'
    const valores=[funcionario.nome,funcionario.cargo,
    funcionario.salario,funcionario.id]
    const retorno=await con.query(sql,valores)
    return retorno[0]
}
//instalação
//arquivo instalação.txt
//após criar a pasta com os arquivos na estrutura abaixo:
