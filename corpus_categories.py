from collections import OrderedDict

#These files are composites of files that already exist in parts in the tesserae corpus
composite_files = {
	'grc/antiphon.speeches.tess',
	'grc/apollonius.argonautica.tess',
	'grc/appian.civil_wars.tess',
	'grc/dionysius_halicarnassensis.antiquitates_romanae.tess',
	'grc/eusebius_caesarea.historia_ecclesiastica.tess',
	'grc/flavius_josephus.antiquitates_judaicae.tess',
	'grc/flavius_josephus.contra_apionem.tess',
	'grc/flavius_josephus.de_bello_judaico_libri_vii.tess',
	'grc/galen.natural_faculties.tess',
	'grc/herodotus.histories.tess',
	'grc/homer.iliad.tess',
	'grc/homer.odyssey.tess',
	'grc/hyperides.speeches.tess',
	'grc/isaeus.speeches.tess',
	'grc/isocrates.letters.tess',
	'grc/isocrates.speeches.tess',
	'grc/lysias.speeches.tess',
	'grc/nonnus_of_panopolis.dionysiaca.tess',
	'grc/oppian.halieutica.tess',
	'grc/oppian_of_apamea.cynegetica.tess',
	'grc/pausanias.description_of_greece.tess',
	'grc/philostratus_the_athenian.vita_apollonii.tess',
	'grc/pindar.odes.tess',
	'grc/plato.epistles.tess',
	'grc/plato.leges.tess',
	'grc/plato.respublica.tess',
	'grc/quintus_smyrnaeus.fall_of_troy.tess',
	'grc/strabo.geography.tess',
	'grc/thucydides.peleponnesian_war.tess',
}

def _get_categories():
	f = open('labels/genre_labels.csv')
	val_to_label = {tok.split(':')[1]: tok.split(':')[0] for tok in f.readline().strip().split(',')}
	f.readline()
	categories = OrderedDict((label, set()) for label in val_to_label.values())
	for line in f:
		line = line.strip().split(',')
		categories[val_to_label[line[1]]].add(line[0])
	return categories

genre_to_files = _get_categories()
