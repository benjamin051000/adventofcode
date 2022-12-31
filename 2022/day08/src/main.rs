fn make_forest(text: &String) -> Vec<Vec<u32>> {
    let mut forest: Vec<Vec<u32>> = text
        .split("\n")
        .map(|line| 
            line
                .chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<_>>()
        )
        .collect();

    // Remove trailing [] if there is one
    if forest.last().unwrap().len() == 0 { forest.pop(); }

    forest
}


// A tree is visible if it is taller than all trees before it (in a particular direction).
// Return number of visible trees in this row.
fn find_visible(row: Vec<u32>) -> Vec<bool> {
    let mut max: i32 = -1;
    let mut visibles = vec![false; row.len()];

    for (idx, tree) in row.iter().enumerate() {
        if *tree as i32 > max {
            max = *tree as i32;
            visibles[idx] = true;
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


/// OR together two 2D vectors.
fn or(a: Vec<Vec<bool>>, b: Vec<Vec<bool>>) -> Vec<Vec<bool>> {
    assert_eq!(a.len(), b.len());
    assert_eq!(a[0].len(), b[0].len());

    let mut result: Vec<Vec<bool>> = vec![vec![false; a[0].len()]; a.len()];

    for r in 0..a.len() {
        for c in 0..a[0].len() {
            result[r][c] = a[r][c] || b[r][c];
        }
    }

    result
}


fn part1(contents: &String) -> u32 {
    let mut forest = make_forest(contents);

    // --------------------------
    // left
    // --------------------------
    let mut vis_from_left = Vec::<Vec<bool>>::new();

    for row in &forest {
        vis_from_left.push(find_visible(row.to_vec()));
    }

    // --------------------------
    // right
    // --------------------------
    let mut vis_from_right = Vec::<Vec<bool>>::new();

    for row in &mut forest {
        row.reverse();
        vis_from_right.push(find_visible(row.to_vec()));
    }
    // Un-reverse right visible array
    for row in &mut vis_from_right {
        row.reverse();
    }

    // --------------------------
    // top
    // --------------------------
    // BUG this isn't working
    let mut forest_t = transpose(forest);

    let mut vis_from_top = Vec::<Vec<bool>>::new();

    for row in &forest_t {
        vis_from_top.push(find_visible(row.to_vec()));
    }
    // Un-transpose vis 
    vis_from_top = transpose(vis_from_top);

    // --------------------------
    // bottom
    // --------------------------
    let mut vis_from_bot = Vec::<Vec<bool>>::new();

    for row in &mut forest_t {
        row.reverse();
        vis_from_bot.push(find_visible(row.to_vec()));
    }
    // Un-transpose and un-reverse vis_from_bot
    vis_from_bot = transpose(vis_from_bot);
    for row in &mut vis_from_bot {
        row.reverse();
    }

    // --------------------------
    // Calculate total
    // --------------------------
    let combined = or(vis_from_left, or(vis_from_right, or(vis_from_top, vis_from_bot)));
    
    combined
        .iter()
        .map(|row| 
            row
                .iter()
                // Just get the true values
                .filter(|x| 
                    **x
                )
                .count() as u32
        )
        .sum()
}


fn part2(contents: &String) -> i32 {
    todo!();
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
                    35390".to_string();

    assert_eq!(part1(&contents), 21);
}

#[test]
fn example2() {

}

