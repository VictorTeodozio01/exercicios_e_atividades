public class ContaPoupanca extends Conta {

    public ContaPoupanca(Cliente cliente) {
        super(cliente);
    }

    @Override
    public void imprimirExtrato() {
        System.out.println("=== Extrato Conta Poupança ===");
        System.out.println("Titular: " + cliente.getNome());
        System.out.println("Número: " + numero);
        System.out.println("Saldo: " + saldo);
    }
}
