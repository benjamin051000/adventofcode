use std::collections::HashMap;

#[derive(Debug, Clone)]
struct File<'a> {
    parent: &'a str,
    size: i64
}

impl<'a> File<'a> {
    fn new(parent: &'a str, size: i64) -> Self {
        File {
            parent,
            size
        }
    }
}

fn get_dir_sizes<'a>(fs: HashMap<&'a str, File<'a>>) -> HashMap<&'a str, i64> {

    let mut dir_sizes = HashMap::<&str, i64>::new();

    // Add sizes from non-directories.
    for (_, file) in &fs {
        dir_sizes
            .entry(file.parent)
            .and_modify(|s| *s += file.size)
            .or_insert(file.size);
    }

    // Add sizes from nested directories.
    for (name, file) in fs.clone() {
        // Get just the directories
        if file.size == 0 {
            // This is a dir.
            // Add its size to its parents.
            let this_dirs_size = *dir_sizes
                .get(name)
                .expect(format!("{name} had 0...").as_str());
            // println!("dir {} is {}", name, this_dirs_size);

            // Add this value to its parents, all the way up to "/".
            let mut fp = name;
            // dbg!(fp);

            let mut i = 0;
            loop {
                fp = &fs.get(fp).unwrap().parent;
                // let file_to_change: &mut File = fs.get_mut(fp).unwrap();
                let file_to_change = dir_sizes.get_mut(fp).unwrap();

                // println!("\tFile to change: {} {:?}", fp, file_to_change);
                // println!("\tAdding {}", this_dirs_size);

                *file_to_change += this_dirs_size;

                // println!("\tNew File: {} {:?}", fp, file_to_change);

                // Move the file pointer up a directory to the next parent.
                if fp == "/" { break; }
                i += 1;
                if i > 1000 {
                    panic!("Something's wrong.");
                }
                // dbg!(fp);
            }
            // println!("-------------------");
        }
    }
    dbg!(&dir_sizes);

    dir_sizes
}


fn part1(contents: &String) -> i64 {
    // Name -> {parent, size}
    let mut fs: HashMap<&str, File> = HashMap::new();
    // Insert root, which is a parent of itself.
    // fs.insert("/", File::new("/", 0));
    let mut fp = "/";

    for line in contents.lines() {
        let tokens: Vec<_> = line.split_whitespace().collect();
        match &tokens[..] {
            ["$", "cd", loc] => {
                // Attempt to "cd" into this dir. If it doesn't exist, make it first.
                // 1. Are we already at loc?
                // NOTE omit this for now since you can have nested files with the same name.

                // Are we going up a directory?
                if *loc == ".." {
                    fp = fs.get(fp).unwrap().parent;
                    dbg!(&fp);
                    continue;
                }

                // Do we need to create this directory?
                match fs.get(loc) {
                    None => {
                        // Create the folder and set fp to it.
                        fs.insert(loc, File::new(fp, 0));
                    },
                    _ => {},
                }
                
                // Set the file pointer to this location.
                fp = loc;
                dbg!(&fp);
            }

            ["$", "ls"] => continue,

            ["dir", dirname] => {
                // Insert this dir inside the current one.
                fs.insert(dirname, File::new(fp, 0));
                println!("Created directory \"{}\" in \"{}\"", dirname, fp);
            }

            [size, name] => {
                fs.insert(name, File::new(fp, size.parse().unwrap()));
                println!("Created file \"{}\" in \"{}\"", name, fp);
            }
            _ => unreachable!()
        }

        // dbg!(&fs);
    }

    let sizes = get_dir_sizes(fs);
    dbg!(&sizes);

    sizes
        .values()
        .filter(|s| **s < 100_000)
        .sum()
}

fn part2(contents: &String) -> i64 {
    0
}

fn main() {
    let contents = std::fs::read_to_string("day07_input.txt").expect("Read file successfully");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[test]
fn example1() {
    let contents = include_str!("../test.txt").to_string();
    assert_eq!(part1(&contents), 95437);
}

#[test]
fn example2() {

}

