use std::collections::{HashMap, HashSet};

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

// TODO another idea is to only count non-dirs, and just add each one to EVERY parent.
// So iterate until you find a non-dir (file with non-zero size), and just add its size
// to each parent all the way up. This is deterministic! Should work!

fn get_dir_sizes(fs: FileSystem) -> HashMap<String, i64> {
    // Get set of dirs (so we know which ones to skip during iteration)
    let all_dirnames = fs
        .iter()
        .filter(|(_, f)| f.size == 0)
        .map(|(name, _)| name.to_string())
        .collect::<HashSet<String>>();

    let mut dir_sizes = HashMap::<String, i64>::new();

    for (name, _) in &fs {
        // Skip if it's a directory.
        if all_dirnames.contains(&name.to_string()) { continue; }

        let this_size: i64 = fs.get(name).unwrap().size;

        // For each file, add its size to each parent up to "/".
        let mut fp = &fs.get(name).unwrap().parent;
        loop {
            // Add to its dir size.
            dir_sizes
                .entry(fp.to_string())
                .and_modify(|sz| *sz += this_size)
                .or_insert(this_size);

            // If we just modified the "/" size, we're done.
            if fp == "/" { break; }
            // Update fp 
            fp = &fs.get(fp).unwrap().parent;
            
        }
    }
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

