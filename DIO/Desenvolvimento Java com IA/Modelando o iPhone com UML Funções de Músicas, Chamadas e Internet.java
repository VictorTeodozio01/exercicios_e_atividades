// Interface ReprodutorMusical
public interface ReprodutorMusical {
    void tocar();
    void pausar();
    void selecionarMusica(String musica);
}

// Interface AparelhoTelefonico
public interface AparelhoTelefonico {
    void ligar(String numero);
    void atender();
    void iniciarCorreioVoz();
}

// Interface NavegadorInternet
public interface NavegadorInternet {
    void exibirPagina(String url);
    void adicionarNovaAba();
    void atualizarPagina();
}

// Classe iPhone implementando as interfaces
public class iPhone implements ReprodutorMusical, AparelhoTelefonico, NavegadorInternet {
    // Implementação dos métodos das interfaces
    @Override
    public void tocar() {
        // Implementação
    }

    @Override
    public void pausar() {
        // Implementação
    }

    @Override
    public void selecionarMusica(String musica) {
        // Implementação
    }

    @Override
    public void ligar(String numero) {
        // Implementação
    }

    @Override
    public void atender() {
        // Implementação
    }

    @Override
    public void iniciarCorreioVoz() {
        // Implementação
    }

    @Override
    public void exibirPagina(String url) {
        // Implementação
    }

    @Override
    public void adicionarNovaAba() {
        // Implementação
    }

    @Override
    public void atualizarPagina() {
        // Implementação
    }
}
