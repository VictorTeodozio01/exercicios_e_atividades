public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("João Silva");
        
        Conta cc = new ContaCorrente(cliente);
        Conta poupanca = new ContaPoupanca(cliente);
        
        Banco banco = new Banco();
        banco.adicionarConta(cc);
        banco.adicionarConta(poupanca);
        
        cc.depositar(1000);
        cc.transferir(200, poupanca);
        
        cc.imprimirExtrato();
        poupanca.imprimirExtrato();
    }
}
