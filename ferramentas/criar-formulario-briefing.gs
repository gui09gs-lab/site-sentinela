/**
 * Cria o Google Forms "Briefing do site" com todas as perguntas,
 * dividido em seções, e uma planilha que recebe as respostas.
 *
 * Como usar:
 * 1. Acesse https://script.google.com com a sua conta Google e clique em "Novo projeto".
 * 2. Apague o código de exemplo, cole este arquivo inteiro e salve (Ctrl+S).
 * 3. No topo, escolha a função "criarFormulario" e clique em "Executar".
 * 4. Autorize o acesso (se aparecer "app não verificado": Avançado > Acessar projeto).
 * 5. Abra "Registro de execução": lá estão o link para enviar ao cliente,
 *    o link para editar o formulário e o link da planilha de respostas.
 */

const NOME_EMPRESA_DESENVOLVEDORA = ''; // opcional: o nome que assina o formulário

function criarFormulario() {
  const form = FormApp.create('Briefing do site · Questionário');
  form.setDescription(
    'Este questionário reúne tudo o que precisamos para trocar o conteúdo de exemplo do site pelas ' +
    'informações reais da sua empresa. O site e o simulador de câmeras já estão prontos; com as suas ' +
    'respostas, ele passa a ter o seu nome, o seu contato, as suas fotos e os seus serviços.\n\n' +
    '• Perguntas obrigatórias estão marcadas com *. As demais podem ser respondidas depois.\n' +
    '• Não sabe responder? Escreva "não sei" ou "me ajude a definir".\n' +
    '• Arquivos (logo, fotos, documentos): envie um link do Google Drive ou WeTransfer nos campos indicados.\n' +
    '• Você pode salvar e editar as respostas depois de enviar.\n' +
    '• Nunca escreva senhas neste formulário.' +
    (NOME_EMPRESA_DESENVOLVEDORA ? '\n\n' + NOME_EMPRESA_DESENVOLVEDORA : '')
  );
  form.setProgressBar(true);
  form.setAllowResponseEdits(true);
  form.setConfirmationMessage('Recebemos suas respostas. Obrigado! Entraremos em contato para os próximos passos.');

  // ---------- helpers ----------
  const curta = (titulo, obrig, ajuda) => { const i = form.addTextItem().setTitle(titulo).setRequired(!!obrig); if (ajuda) i.setHelpText(ajuda); return i; };
  const longa = (titulo, obrig, ajuda) => { const i = form.addParagraphTextItem().setTitle(titulo).setRequired(!!obrig); if (ajuda) i.setHelpText(ajuda); return i; };
  const unica = (titulo, opcoes, obrig, ajuda, outro) => { const i = form.addMultipleChoiceItem().setTitle(titulo).setChoiceValues(opcoes).setRequired(!!obrig); if (outro) i.showOtherOption(true); if (ajuda) i.setHelpText(ajuda); return i; };
  const varias = (titulo, opcoes, obrig, ajuda, outro) => { const i = form.addCheckboxItem().setTitle(titulo).setChoiceValues(opcoes).setRequired(!!obrig); if (outro) i.showOtherOption(true); if (ajuda) i.setHelpText(ajuda); return i; };
  const secao = (titulo, ajuda) => { const p = form.addPageBreakItem().setTitle(titulo); if (ajuda) p.setHelpText(ajuda); return p; };
  const SIM_NAO = ['Sim', 'Não'];

  // ---------- 1. Dados da empresa ----------
  form.addSectionHeaderItem().setTitle('1. Dados da empresa').setHelpText('Aparecem no topo, no rodapé e na política de privacidade do site.');
  curta('Nome da empresa como deve aparecer no site (nome fantasia)', true);
  curta('Razão social', true);
  curta('CNPJ', true);
  curta('Slogan ou frase que resume a empresa', false, 'Ex.: "Segurança que se antecipa"');
  curta('Ano de fundação');
  curta('Endereço completo (se atende clientes no local)');
  unica('O endereço pode aparecer no site?', ['Sim, completo', 'Só a cidade', 'Não']);
  longa('História da empresa em 3 a 5 frases', false, 'Como começou, quem fundou, o que mudou desde então.');
  curta('Nome e cargo do responsável, se quiser aparecer no site');
  longa('Quantas pessoas trabalham na empresa? A equipe de instalação é própria ou terceirizada?');
  curta('Possui alvará, registro ou licença específica de segurança eletrônica? Qual?');

  // ---------- 2. Contato ----------
  secao('2. Contato e atendimento', 'O formulário do site, o botão flutuante e o simulador enviam mensagens prontas para o WhatsApp informado aqui.');
  curta('WhatsApp que vai receber os pedidos (com DDD)', true);
  curta('Telefone fixo ou de atendimento, se for diferente', false);
  curta('E-mail de contato comercial', true).setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  curta('Horário de atendimento comercial', false, 'Ex.: seg a sex, 8h às 18h; sáb 8h às 12h');
  curta('Existe atendimento de emergência ou plantão 24h? Em qual número?');
  curta('Em quanto tempo vocês costumam responder um novo contato?', false, 'O site promete "resposta em poucos minutos".');
  longa('Mensagem de boas-vindas que o cliente deve ver ao abrir o WhatsApp (opcional)');
  curta('Instagram (@)');
  curta('Facebook (link)');
  curta('YouTube, TikTok ou LinkedIn (links)');
  curta('Perfil no Google Meu Negócio (link)');
  curta('Algum canal que NÃO deve aparecer no site?');

  // ---------- 3. Serviços ----------
  secao('3. Nicho e serviços');
  varias('Quais serviços vocês oferecem?', [
    'Instalação de câmeras (CFTV)', 'Alarmes e sensores de presença ou abertura', 'Monitoramento 24h com central própria',
    'Acesso às câmeras pelo celular (aplicativo)', 'Gravação em nuvem', 'Manutenção preventiva e corretiva', 'Cerca elétrica',
    'Interfone, vídeo porteiro ou controle de acesso', 'Fechadura digital', 'Portaria remota (condomínios)', 'Motor de portão',
    'Rede, Wi-Fi ou cabeamento estruturado'], true, null, true);
  longa('Comente os serviços marcados: como funcionam e qual o diferencial de cada um');
  curta('Qual é o serviço principal, o que mais vende?', true);
  varias('Quem vocês atendem?', ['Residências', 'Condomínios', 'Comércio', 'Empresas e indústrias'], true, null, true);
  curta('Quais marcas de equipamento vocês trabalham?', false, 'Ex.: Intelbras, Hikvision, Dahua');
  curta('Qual aplicativo o cliente usa para ver as câmeras?');
  unica('Vocês vendem o equipamento ou alugam em comodato?', ['Vendemos', 'Alugamos em comodato', 'Os dois']);
  longa('Existe plano mensal de monitoramento? Como funciona e o que inclui?');
  curta('Garantia oferecida (equipamento e instalação)');
  unica('A visita técnica e o orçamento são gratuitos?', SIM_NAO, true);
  curta('Prazo médio entre fechar o contrato e instalar', true, 'O site diz "até 48h".');
  curta('Formas de pagamento e parcelamento');
  longa('Faixa de preço de um kit básico residencial (ex.: 4 câmeras + gravador). Pode aparecer no site?');

  // ---------- 4. Público e região ----------
  secao('4. Público e região', 'Quem procura segurança quer uma empresa perto de casa. Essas respostas também ajudam o Google a mostrar vocês nas buscas da região.');
  longa('Cidades e bairros atendidos', true);
  curta('Existe taxa ou distância máxima para atendimento?');
  longa('Quem é o cliente típico?', false, 'Ex.: famílias em casas térreas, condomínios fechados, pequenos comércios');
  curta('Faixa de renda ou perfil do bairro mais comum');
  longa('Quais são as 3 principais preocupações que os clientes trazem?', false, 'Ex.: furto na garagem, filhos sozinhos em casa, viagens');
  longa('Que perguntas os clientes sempre fazem antes de fechar?');
  longa('Por que um cliente desiste de fechar?', false, 'Preço, desconfiança, prazo...');
  longa('Quem são os principais concorrentes na região? (nomes ou sites)');
  longa('Algum site de empresa (de qualquer ramo) que você admira? Por quê?');

  // ---------- 5. Diferenciais e prova social ----------
  secao('5. Diferenciais, números e prova social', 'O site só pode mostrar números e depoimentos verdadeiros.');
  form.addGridItem().setTitle('Os números de exemplo do site estão corretos?')
    .setRows(['24h de monitoramento, todos os dias', '48h de prazo médio de instalação', '30 dias de gravação em nuvem', 'Visita técnica e orçamento grátis'])
    .setColumns(['Correto', 'Corrigir', 'Remover']).setRequired(true);
  longa('Se marcou "Corrigir", informe os números reais');
  longa('Em 3 frases: por que o cliente deve escolher vocês e não o concorrente?', true);
  curta('Quantos clientes ou instalações já foram feitos?');
  curta('Quantos anos de experiência a equipe tem?');
  curta('Quantas câmeras ou sistemas estão ativos hoje?');
  curta('Nota e número de avaliações no Google', false, 'Ex.: 4,9 com 120 avaliações');
  longa('3 a 5 depoimentos reais: nome (ou iniciais), bairro e o texto', false, 'Informe se o cliente autorizou o uso.');
  longa('Certificações da equipe ou parcerias com fabricantes');
  longa('Algum caso real que vale contar?', false, 'Ex.: furto evitado ou imagem que ajudou a polícia, sem expor ninguém.');
  longa('Clientes empresariais conhecidos que autorizam aparecer o logo');

  // ---------- 6. Identidade visual ----------
  secao('6. Identidade visual', 'Hoje o site usa vermelho (#E11D2E), fundo claro e a fonte Manrope. Se a empresa já tem identidade, o site passa a seguir a dela.');
  unica('Tem logotipo?', ['Sim', 'Não, preciso de um'], true);
  curta('Link do logotipo (Google Drive, WeTransfer)', false, 'Ideal em vetor (SVG, PDF, AI, EPS) ou PNG com fundo transparente. Se tiver, inclua a versão para fundo escuro e só o símbolo.');
  curta('Cores da marca', false, 'Código HEX, Pantone ou descreva');
  curta('Fontes usadas no material da empresa, se souber');
  curta('Link do manual de marca, se existir');
  unica('O vermelho atual combina com a empresa?', ['Sim, pode manter', 'Prefiro outra cor (informe abaixo)']);
  curta('Se prefere outra cor principal, qual?');
  unica('Estilo desejado', ['Mais corporativo e sério', 'Mais moderno e tecnológico', 'Mais próximo e familiar'], false, null, true);
  curta('Link de fotos do uniforme, carro adesivado ou fachada');
  longa('Algo que você NÃO quer ver no site (cores, palavras, tipo de foto)?');

  // ---------- 7. Fotos e conteúdo ----------
  secao('7. Fotos e conteúdo', 'Fotos reais passam muito mais confiança que fotos de banco de imagens. Tiradas com celular, na horizontal e com boa luz, já servem.');
  varias('Quais fotos você consegue enviar?', [
    'Equipe uniformizada', 'Técnico instalando uma câmera', 'Câmeras instaladas em casas de clientes (sem número da casa ou rosto de morador)',
    'Tela do aplicativo com as câmeras (sem imagens de clientes reais)', 'Carro da empresa, fachada ou sala de monitoramento',
    'Equipamentos: câmeras, gravador, sensores', 'Foto do responsável']);
  curta('Link da pasta com as fotos');
  unica('As pessoas que aparecem nas fotos autorizaram o uso?', ['Sim', 'Não', 'Não se aplica']);
  unica('As fotos de imóveis têm autorização dos donos?', ['Sim', 'Não', 'Não se aplica']);
  unica('Prefere contratar um fotógrafo para uma sessão?', SIM_NAO);
  curta('Links de vídeo institucional ou vídeos de instalação');
  longa('Algum texto pronto que deve ser usado (apresentação, missão, panfleto)?');
  longa('Perguntas frequentes', false, 'O site tem 4: câmeras funcionam à noite, ver no celular, falta de internet ou energia, quanto custa. Confirme e acrescente outras com a resposta.');
  longa('O sistema tem nobreak? Continua gravando se faltar internet ou energia?');

  // ---------- 8. Simulador ----------
  secao('8. Simulador de câmeras', 'No simulador, o visitante desenha a casa, posiciona as câmeras e envia o projeto pelo WhatsApp. Com os dados dos modelos que vocês vendem, a simulação fica fiel ao que será instalado.');
  const MOD = 'Marca e modelo; lente (mm); ângulo horizontal (°); alcance do infravermelho (m); resolução; uso (interna/externa); preço instalado (R$). Deixe em branco se não vende.';
  longa('Câmera Bullet', false, MOD);
  longa('Câmera Dome', false, MOD);
  longa('Câmera Speed Dome / PTZ', false, MOD);
  longa('Câmera Panorâmica 360°', false, MOD);
  longa('Outros modelos', false, MOD);
  unica('O simulador deve mostrar uma estimativa de preço?', ['Sim', 'Não', 'Só "a partir de"']);
  longa('Custos fixos do projeto', false, 'Gravador (DVR/NVR), HD, cabeamento, mão de obra, taxa de visita');
  longa('Existem pacotes prontos?', false, 'Ex.: "Kit Casa 4 câmeras", o que inclui e o preço');
  varias('Plantas modelo que fazem sentido para a sua região', ['Casa térrea', 'Sobrado', 'Casa de condomínio', 'Apartamento', 'Comércio'], false, null, true);
  longa('Regras de recomendação que vocês usam', false, 'Ex.: "todo portão leva uma Bullet", "sala ampla leva 360°"');
  varias('Quais dados o visitante deve informar antes de enviar o projeto?', ['Nome', 'Telefone / WhatsApp', 'Bairro', 'Tipo de imóvel', 'Melhor horário para contato'], false, null, true);
  curta('Quem recebe esses projetos e em quanto tempo responde?');

  // ---------- 9. Domínio e hospedagem ----------
  secao('9. Domínio, hospedagem e acessos', 'O domínio é o endereço do site (ex.: suaempresa.com.br). O ideal é que fique registrado no nome ou CNPJ da sua empresa. NUNCA escreva senhas aqui: combinamos os acessos por ligação.');
  unica('Já tem domínio registrado?', SIM_NAO, true);
  curta('Se tem, qual é o domínio?');
  longa('Se não tem, 3 opções de endereço em ordem de preferência');
  curta('O domínio está registrado em nome de quem (pessoa ou CNPJ)? Você tem o login do registro.br?');
  curta('Já existe um site no ar? Qual endereço e onde está hospedado?');
  curta('Usa e-mail com o domínio? Em qual serviço (Google Workspace, Hostinger, outro)?');
  unica('Onde prefere a hospedagem?', ['Na minha conta', 'Na conta de vocês, dentro do plano de manutenção', 'Não sei, me ajude a definir']);
  curta('Quem deve receber os avisos técnicos (renovação de domínio, problemas no site)?');

  // ---------- 10. Formulário e integrações ----------
  secao('10. Formulário, contatos e integrações', 'Hoje o formulário do site abre o WhatsApp com a mensagem pronta e não guarda nenhum dado.');
  varias('Por onde os pedidos devem chegar?', ['WhatsApp', 'E-mail', 'Sistema de vendas / CRM'], false, null, true);
  curta('Usa algum sistema de vendas ou CRM? Qual?', false, 'Ex.: RD Station, Pipedrive, planilha');
  longa('Quer acrescentar campos ao formulário do site?', false, 'Hoje: nome, WhatsApp e tipo de imóvel. Ex.: bairro, melhor horário, como conheceu a empresa');
  varias('Vai anunciar em quais canais?', ['Google', 'Instagram / Facebook', 'Ainda não sei', 'Não vou anunciar']);
  longa('IDs do Google Analytics, Google Ads ou Meta, se já tiver', false, 'Envie apenas os IDs, nunca senhas.');
  unica('Quer receber um relatório mensal de visitas e contatos do site?', SIM_NAO);
  unica('Quer um chat automático ou robô no WhatsApp?', SIM_NAO);
  unica('Tem cadastro no Google Meu Negócio?', ['Sim', 'Não, quero ajuda para criar', 'Sim, quero ajuda para otimizar']);

  // ---------- 11. Jurídico e LGPD ----------
  secao('11. Jurídico e LGPD', 'Como o site coleta nome e telefone, ele precisa de uma política de privacidade de acordo com a LGPD.');
  curta('Link da política de privacidade ou dos termos de uso, se já tiver');
  curta('Responsável pelos dados pessoais na empresa (encarregado ou DPO): nome e e-mail');
  curta('Por quanto tempo vocês guardam os dados de quem pede orçamento?');
  curta('Como os clientes podem pedir para apagar os seus dados? (e-mail ou WhatsApp)');
  unica('Existe advogado ou contador que deve revisar os textos legais antes de publicar?', SIM_NAO);
  longa('Há alguma promessa que NÃO pode ser feita no site?', false, 'Ex.: "garantia de segurança total", "resposta imediata"');

  // ---------- 12. Encerramento ----------
  secao('12. Para finalizar');
  varias('O que você já enviou ou vai enviar?', [
    'Logotipo', 'Fotos reais', 'Depoimentos com autorização', 'Tabela de modelos e preços para o simulador',
    'Links das redes sociais', 'Manual de marca', 'Política de privacidade', 'IDs de Analytics / Ads']);
  longa('Algo mais que devemos saber?');
  curta('Seu nome e cargo (quem respondeu este questionário)', true);

  // ---------- planilha de respostas ----------
  const ss = SpreadsheetApp.create('Respostas · Briefing do site');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Link para enviar ao cliente: ' + form.getPublishedUrl());
  Logger.log('Link para editar o formulário: ' + form.getEditUrl());
  Logger.log('Planilha de respostas: ' + ss.getUrl());
}
