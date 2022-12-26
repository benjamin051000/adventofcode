use std::{collections::HashMap, mem::needs_drop};

#[derive(Debug, Clone)]
struct File {
    parent: String,
    size: i64
}

impl File {
    fn new(parent: String, size: i64) -> Self {
        File { parent, size }
    }
}


// Full name of file/dir -> {Parent's full name, Size}
type FileSystem = HashMap<String, File>;

// BUG: This will sometimes double-count subdirs.
// For example, /a/e/ is added to /, but later, /a will add to /, which double-counts e.
// Not sure how to fix this, so ignore it for now lol
fn get_dir_sizes(fs: FileSystem) -> HashMap<String, i64> {
    let mut dir_sizes = HashMap::<String, i64>::new();

    // Add sizes from non-directories.
    for (_, file) in &fs {
        dir_sizes
            .entry(file.parent.to_string())
            .and_modify(|s| *s += file.size)
            .or_insert(file.size);
    }

    // Add sizes from nested directories.
    for (name, file) in fs.clone() {
        // Skip /, which will be updated automatically by other ones.
        if name == "/" {
            println!("Skipping root");
            continue;
        }

        // Get just directories
        if file.size == 0 {
            println!("Found dir \"{name}\" size {}. Updating parents...", file.size);
            let child_dirs_size: i64 = *dir_sizes
                .get(&name)
                .expect(format!("{name} was in dir_sizes with size 0").as_str());

            // Add its size to each of its parents up to "/".

            // File pointer starts at this file.
            let mut fp: String = name;
            let mut timeout_counter = 0;

            loop {
                // Update file pointer to the current file's parent.
                print!("fp: {fp} -> ");
                fp = fs.get(&fp).unwrap().parent.to_string();
                println!("{fp}");

                // Get dir to change
                let dir_to_change = dir_sizes.get_mut(&fp).unwrap();

                // println!("\tFile to change: {} {:?}", fp, file_to_change);
                // println!("\tAdding {}", this_dirs_size);

                *dir_to_change += child_dirs_size;

                // println!("\tNew File: {} {:?}", fp, file_to_change);

                // Move the file pointer up a directory to the next parent.
                if fp == "/" { 
                    // println!("Done updating parents.");
                    break; 
                }

                // Update timeout counter
                timeout_counter  += 1;
                if timeout_counter > 1000 {
                    panic!("Something's wrong.");
                }
                // dbg!(fp);
            } // end of loop

        } // end of if file.size == 0
    } // end of for

    dir_sizes
}

/// Make the filesystem and return it.
fn mkfs(contents: &String) -> FileSystem {
    let mut fs = FileSystem::new();
    
    // Current working directory.
    let mut full_path = Vec::<String>::new();

    for line in contents.lines() {
        // Update the cwd.
        let cwd: String = full_path.join("/");

        let tokens: Vec<_> = line.split_whitespace().collect();
        match &tokens[..] {
            ["$", "cd", loc] => {
                // 1. move up if .. and not just ["/"]
                if *loc == ".." && full_path.len() > 1 {
                    full_path.pop();
                }
                else {
                    // 2. Move there from cwd, mkdir if necessary
                    full_path.push(loc.to_string());

                    // Mkdir if it doesn't already exist
                    let new_dir_path = full_path.join("/");
                    if cwd != "" {
                        fs.entry(new_dir_path).or_insert(File::new(cwd, 0)); // TODO verify this works as expected
                    }
                    else {
                        fs.entry(new_dir_path).or_insert(File::new("/".to_string(), 0)); // TODO verify this works as expected
                    }
                }
            },

            ["$", "ls"] => continue,

            ["dir", dirname] => {
                // Create directory at cwd
                let abs_filename = cwd.clone() + "/" + dirname;
                fs.insert(abs_filename, File::new(cwd, 0));
            },

            [filesize, filename] => {
                // Add this file at cwd.
                let abs_filename = cwd.clone() + "/" + filename;
                fs.insert(abs_filename, File::new(cwd, filesize.parse().unwrap()));
            },

            _ => unreachable!(),

        } // end of match &tokens[..]
    } // end of for line in contents.lines()

    fs
}


fn part1(contents: &String) -> i64 {
    let fs = mkfs(contents);
    // dbg!(&fs);

    let sizes = get_dir_sizes(fs);
    // dbg!(&sizes);

    sizes
        .values()
        .filter(|s| **s < 100_000)
        .sum()
}

fn part2(contents: &String) -> i64 {
    const REQD_SPACE: i64 = 30000000;
    const TOTAL_SPACE: i64 = 70000000;

    let fs = mkfs(contents);
    // dbg!(&fs);

    let sizes = get_dir_sizes(fs);

    let current_space = sizes.get("/").unwrap();
    let current_free = TOTAL_SPACE - current_space;
    let need_to_free_up = REQD_SPACE - current_free;

    // Find the smallest one greater than (>=) need_to_free_up
    *sizes
        .values()
        .filter(|i| **i >= need_to_free_up)
        .min()
        .unwrap()
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
fn test_example_sizes() {
    let contents = include_str!("../test.txt").to_string();
    let fs = mkfs(&contents);
    let sizes = get_dir_sizes(fs);
    assert_eq!(*sizes.get("//a/e").unwrap(), 584, "testing /a/e");
    assert_eq!(*sizes.get("//a").unwrap(), 94853, "testing /a");
    assert_eq!(*sizes.get("//d").unwrap(), 24933642, "testing /d");
    assert_eq!(*sizes.get("/").unwrap(), 48381165, "testing /");
}

#[test]
fn example2() {
    let contents = include_str!("../test.txt").to_string();
    assert_eq!(part2(&contents), 24933642);
}

