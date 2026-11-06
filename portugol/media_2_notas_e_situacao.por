programa {
  funcao inicio() {
    real nota1,nota2,media
    escreva("Informe a 1a nota: ")
    leia(nota1)
    escreva("Informe a 2ª nota: ")
    leia(nota2)
    media=(nota1+nota2)/2
    escreva("A média é: ",media,"\n")
    se(media>=7) {
      escreva("\nAprovado(a)")
      escreva("\nPARABÉNS!")
    }
    senao
      escreva("Recuperação")
  }
}
