# askBreno
Skill da Alexa para auxiliar os estudantes de Sistemas de Informação da Universidade Tocantins com os cronogramas da instituição
## Autor: Patrick Aires Barros 

## Propósito
Atraveś do uso da Alexa e da coleta de dados das informações sobre o curso orientar os alunos sobre aulas, matérias e professores.

## Público
Todos os alunos de Sistemas de Informação.

## Principais funcionalidades (intent) e descrição
### HorarioIntent:
Falar sobre as matérias que ocorrem nesse dia.
### MateriaIntent:
Descrição da Matéria / Quem irá aplica-la.
### ProfessorIntent:
Matérias que o professor irá aplicar.

## Mapa de intent (exemplo de gatilho, variáveis e retorno esperado)
#### HorarioIntent:
gatilho: "Qual o horario do sexto período" 
#####
variaveis: horario, periodo
#####
retorno: "As materias disponiveis para este periodo são: "
#####
#### MateriaIntent:
gatilho: "Qual o horario do da materia x?"
#####
variaveis: materia, diaDaSemana, professor
#####
retorno: "O horario de {} é na(o) {} com a(o) professor(a) {}", materia, diaDaSemana, professor
#####
#### ProfessorIntent:
gatilho: "Que matéria o professor {} dá?", "Que dia o professor {} dá aula?"
#####
variaveis: professor, materia, diaDaSemana
#####
retorno: "O professor(a) {} dá aula(s) de {} na {}, [...]", professor, materia, diaDaSemana