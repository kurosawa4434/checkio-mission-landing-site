from typing import Set

def landing_site(obstacles: Set[str]) -> Set[str]:
    return set()


if __name__ == '__main__':
    assert landing_site({'E5', 'E7', 'F4', 'F6', 'G4', 'G6', 'H3', 'H5'}) == {'C3', 'J7'}, 'crevasse'
    assert landing_site({'A4', 'C2', 'C6', 'C9', 'D4', 'D7', 'F1', 'F5',
                         'F8', 'G4', 'H7', 'I2', 'I5', 'I9', 'K3', 'K8', 'L5'}) == {'B7', 'E3', 'J6'}, 'stones'
    assert landing_site({'D3', 'D4', 'D5', 'D6', 'E3', 'E7', 'F2', 'F7', 'G2',
                         'G8', 'H2', 'H7', 'I3', 'I7', 'J3', 'J4', 'J5', 'J6'}) == {'G5'}, 'crater'
    assert landing_site(set()) == {'E5', 'F5', 'G5', 'H5'}, 'plane'
    assert landing_site({chr(c+65)+str(r+1) for c in range(12) for r in range(9)}) == set(), 'wasteland'

    print('The local tests are done. Click on "Check" for more real tests.')
