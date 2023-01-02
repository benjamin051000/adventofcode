use std::collections::HashSet;
use itertools::Either;

type Forest = Vec<Vec<u32>>;

fn make_forest(text: &String) -> Forest {
    let mut forest: Forest = text
        .split("\n")
        .map(|line| 
            line
                .chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<_>>()
        )
        .collect();

    // Remove trailing [] if there is one
    // which would have come from a trailing "\n" 
    // so it's okay to remove.
    if forest.last().unwrap().len() == 0 { forest.pop(); }

    forest
}


// A tree is visible if it is taller than all trees before it (in a particular direction).
// Return number of visible trees in this row.
fn find_visibles(
    forest: &Forest, 
    is_transpose: bool,
    rows: &Either<impl Iterator<Item = usize> + Clone, impl Iterator<Item = usize> + Clone>, 
    cols: &Either<impl Iterator<Item = usize> + Clone, impl Iterator<Item = usize> + Clone>) 
-> HashSet<(usize, usize)> {
    // let mut visibles = vec![false; row.len()];
    let mut visibles = HashSet::new();

    for r in rows.clone() {
        let mut max: i32 = -1;

        for c in cols.clone() {
            let tree = forest[r][c];


            if tree as i32 > max {
                max = tree as i32;
                if is_transpose {
                    visibles.insert((c, r)); // Un-flip it
                }
                else {
                    visibles.insert((r, c));
                }

            }
        }
    }

    visibles
}


fn transpose<T: Clone>(v: Vec<Vec<T>>) -> Vec<Vec<T>> {
    assert!(!v.is_empty());

    (0..v[0].len())
        .map(|i| v .iter()
                .map(|inner| 
                    inner[i]
                        .clone()
                )
                .collect::<Vec<T>>()
        )
        .collect()
}


fn create_range(lo: usize, hi: usize) 
-> Either<impl Iterator<Item = usize> + Clone, impl Iterator<Item = usize> + Clone> {
    assert_ne!(lo, hi);
    let rev = lo > hi;

    if !rev {
        Either::Left(lo..hi)
    } else {
        Either::Right((hi..lo).rev())
    }
}

fn part1(contents: &String) -> u32 {
    let forest = make_forest(contents);

    let row_normal = create_range(0, forest.len());
    let col_normal = create_range(0, forest[0].len());

    let col_rev = create_range(forest[0].len(), 0);

    // horizontal views
    let vis_from_left = find_visibles(&forest, false, &row_normal, &col_normal);
    let vis_from_right = find_visibles(&forest, false, &row_normal, &col_rev);

    // For vertical views, look at the forest's transpose.
    let forest_t = transpose(forest);

    let vis_from_top = find_visibles(&forest_t, true, &row_normal, &col_normal);
    let vis_from_bot = find_visibles(&forest_t, true, &row_normal, &col_rev);

    // Get the union of each one (to avoid duplicates)
    let total = &(&(&vis_from_left | &vis_from_right) | &vis_from_top) | &vis_from_bot;

    // Part 1 is the length of these
    total.len() as u32
}


fn get_scenery_score(forest: &Forest, (this_r, this_c): (usize, usize)) -> u32 {

    let rows = forest.len();
    let cols = forest[0].len();

    let this_tree = forest[this_r][this_c];

    let mut west_score = 0;
    for c in (0..this_c).rev() {
        west_score += 1;

        let tree = forest[this_r][c];
        if tree >= this_tree {
            break;
        }
    }

    let mut south_score = 0;
    for r in this_r+1..rows {
        south_score += 1;

        let tree = forest[r][this_c];
        if tree >= this_tree {
            break;
        }
    }

    let mut north_score = 0;
    for r in (0..this_r).rev() {
        north_score += 1;

        let tree = forest[r][this_c];
        if tree >= this_tree {
            break;
        }
    }

    let mut east_score = 0;
    for c in this_c+1..cols {
        east_score += 1;

        let tree = forest[this_r][c];
        if tree >= this_tree {
            break;
        }
    }

    west_score * south_score * north_score * east_score
}


fn part2(_contents: &String) -> u32 {
    let forest = make_forest(_contents);

    let mut max = 0;

    for r in 0..forest.len() {
        for c in 0..forest[0].len() {
            let score = get_scenery_score(&forest, (r, c));
            if score > max {
                max = score;
            }
        }
    }

    max
}


fn main() {
    let contents = std::fs::read_to_string("day08_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}


#[test]
fn example1() {
    let contents = "30373\n\
                    25512\n\
                    65332\n\
                    33549\n\
                    35390\n".to_string();

    assert_eq!(part1(&contents), 21);
}

#[test]
fn example2() {
    let contents = "30373\n\
                    25512\n\
                    65332\n\
                    33549\n\
                    35390\n".to_string();

    assert_eq!(part2(&contents), 8);
}

#[test]
fn test_scene_scores() {
    let contents = "30373\n\
                    25512\n\
                    65332\n\
                    33549\n\
                    35390\n".to_string();

    let forest = make_forest(&contents);

    assert_eq!(get_scenery_score(&forest, (1, 2)), 4);
    assert_eq!(get_scenery_score(&forest, (3, 2)), 8);
}
