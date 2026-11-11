"""Public Basamak Skills packaging and installation smoke checks (not AI behavior tests)."""
from pathlib import Path
import os
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
NAMES = {
    "web-audit", "technical-troubleshooter", "support-assistant",
    "code-reviewer", "software-planner", "conversion-optimizer",
    "saas-positioning", "pricing-review", "automation-discovery",
    "workflow-architect", "ai-feasibility", "release-readiness",
    "subscription-lifecycle",
}
INSTALL = ROOT / "scripts" / "install.sh"
VERSION = "1.2.0"


class Tests(unittest.TestCase):
    def test_skills(self):
        self.assertEqual({p.name for p in SKILLS.iterdir() if p.is_dir()}, NAMES)
        for name in NAMES:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"))
            self.assertIn(f"name: {name}\n", text.split("---\n", 2)[1])
            self.assertIn("description: >-\n", text.split("---\n", 2)[1])

    def test_docs(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), VERSION)
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text())
        for path in (
            "README.md", "README.tr.md", "docs/installation.md", "docs/kurulum.md",
            "CHANGELOG.md", "workflows/feature-request-to-review.md",
            "workflows/feature-request-to-review.tr.md",
            "workflows/automation-opportunity-to-design.md",
            "workflows/automation-opportunity-to-design.tr.md"
        ):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotIn(
            "basamak-ai-skills/.agents",
            (ROOT / "workflows/feature-request-to-review.md").read_text(),
        )
        for path in ("README.md", "README.tr.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertIn(VERSION, text)
            self.assertIn("13", text)
            for name in NAMES:
                self.assertIn(name, text)

    def test_bilingual_skill_pairs(self):
        for name in NAMES:
            with self.subTest(name=name):
                folder = SKILLS / name
                english = (folder / "SKILL.md").read_text(encoding="utf-8")
                turkish = (folder / "SKILL.tr.md").read_text(encoding="utf-8")
                self.assertTrue(english.startswith("---\n"))
                self.assertTrue(turkish.startswith("---\n"))
                self.assertIn(f"name: {name}\n", english)
                self.assertIn(f"name: {name}\n", turkish)
                self.assertIn("description: >-\n", english)
                self.assertIn("description: >-\n", turkish)
                self.assertGreater(len(english), 1200)
                self.assertGreater(len(turkish), 1200)
                self.assertNotEqual(english, turkish)

    def test_workflows_bilingual(self):
        en = (ROOT / "workflows" / "feature-request-to-review.md").read_text(encoding="utf-8")
        tr = (ROOT / "workflows" / "feature-request-to-review.tr.md").read_text(encoding="utf-8")
        for name in ("support-assistant", "software-planner", "code-reviewer"):
            self.assertIn(name, en)
            self.assertIn(name, tr)
        self.assertIn("Stage 4", en)
        self.assertIn("Aşama 4", tr)
        for path in ("workflows/automation-opportunity-to-design.md",
                     "workflows/automation-opportunity-to-design.tr.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            for name in ("automation-discovery", "ai-feasibility", "workflow-architect"):
                self.assertIn(name, text)

    def test_bash_syntax(self):
        subprocess.run(["bash", "-n", str(INSTALL)], check=True)

    def test_user_install_twice(self):
        with tempfile.TemporaryDirectory() as home:
            env = os.environ.copy()
            env["HOME"] = home
            for _ in range(2):
                subprocess.run(["bash", str(INSTALL), "--user"], env=env,
                               capture_output=True, text=True, check=True)
            for name in NAMES:
                link = Path(home) / ".agents" / "skills" / name
                self.assertTrue(link.is_symlink())
                self.assertEqual(link.resolve(), (SKILLS / name).resolve())

    def test_project_install(self):
        with tempfile.TemporaryDirectory() as project:
            subprocess.run(["bash", str(INSTALL), "--project", project],
                           check=True, capture_output=True, text=True)
            for name in NAMES:
                self.assertTrue((Path(project) / ".agents" / "skills" / name).is_symlink())

    def test_conflict_does_not_partially_install(self):
        with tempfile.TemporaryDirectory() as home:
            target = Path(home) / ".agents" / "skills"
            target.mkdir(parents=True)
            (target / "software-planner").mkdir()
            env = os.environ.copy()
            env["HOME"] = home
            p = subprocess.run(["bash", str(INSTALL), "--user"], env=env,
                               capture_output=True, text=True)
            self.assertNotEqual(p.returncode, 0)
            for name in NAMES - {"software-planner"}:
                self.assertFalse((target / name).exists())


if __name__ == "__main__":
    unittest.main()
