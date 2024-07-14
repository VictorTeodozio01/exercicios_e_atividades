public class ContaCorrente extends Conta {

    public ContaCorrente(Cliente cliente) {
        super(cliente);
    }

    @Override
    public void imprimirExtrato() {
        System.out.println("=== Extrato Conta Corrente ===");
        System.out.println("Titular: " + cliente.getNome());
        System.out.println("Número: " + numero);
        System.out.println("Saldo: " + saldo);
    }
}
