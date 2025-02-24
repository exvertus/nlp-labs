import pytest
import eq.ngram_models

@pytest.fixture
def example_lamantia():
    text = \
    """I hear him, see him—interpenetrate
    those shadows warping the garden pathways
    as the dark steps I climb are lit up
    by his Eye magnetic to the moon,
    his Eye magnetic to the moon."""
    return text

@pytest.fixture
def example_frost():
    text = \
    """Two roads diverged in a yellow wood,
       And sorry I could not travel both
       And be one traveler, long I stood
       And looked down one as far as I could
       To where it bent in the undergrowth;
       
       Then took the other, as just as fair,
       And having perhaps the better claim,
       Because it was grassy and wanted wear;
       Though as for that the passing there
       Had worn them really about the same,
       
       And both that morning equally lay
       In leaves no step had trodden black.
       Oh, I kept the first for another day!
       Yet knowing how way leads on to way,
       I doubted if I should ever come back.
       
       I shall be telling this with a sigh
       Somewhere ages and ages hence:
       Two roads diverged in a wood, and I—
       I took the one less traveled by,
       And that has made all the difference."""
    return text

def test_guided_babbler(example_frost):
    frost_babbler = eq.ngram_models.GuidedBabbler(example_frost)

@pytest.fixture
def leaves_of_grass():
    from nltk.corpus import gutenberg
    return gutenberg.raw('whitman-leaves.txt')

@pytest.mark.skip
def test_simple_markov(leaves_of_grass):
    genesis_babbler = eq.ngram_models.SimpleBabbler(leaves_of_grass)
    gen_babble = genesis_babbler.babble(100)
    print(gen_babble)