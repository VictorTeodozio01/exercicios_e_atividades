public class Banco {
    private List<Conta> contas;

    public Banco() {
        this.contas = new ArrayList<>();
    }

    public void adicionarConta(Conta conta) {
        contas.add(conta);
    }

    public Conta buscarContaPorNumero(int numero) {
        return contas.stream()
                     .filter(conta -> conta.getNumero() == numero)
                     .findFirst()
                     .orElse(null);
    }
}
