# GitHub Setup Guide

This guide will help you set up the GitHub repository with environments and release-please for the CI/CD learning project.

## 🚀 **Step 1: Create GitHub Repository**

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `calculator-api` or similar
3. Make it public or private (your choice)
4. **Don't** initialize with README, .gitignore, or license (we'll push our own)

## 🏗️ **Step 2: Set Up GitHub Environments**

### **Development Environment**
1. Go to your repository → Settings → Environments
2. Click "New environment"
3. Name: `development`
4. **Protection rules**: None (auto-deploy)
5. Click "Configure environment"

### **UAT Environment**
1. Click "New environment"
2. Name: `uat`
3. **Protection rules**: None (auto-deploy)
4. Click "Configure environment"

### **Production Environment**
1. Click "New environment"
2. Name: `production`
3. **Protection rules**: 
   - ✅ "Required reviewers" (add yourself)
   - ✅ "Wait timer" (optional: 5 minutes)
4. Click "Configure environment"

## 🔑 **Step 3: Add Required Secrets**

1. Go to Settings → Secrets and variables → Actions
2. Add the following secrets:

### **SONAR_TOKEN** (Required for SonarCloud)
1. Go to [SonarCloud](https://sonarcloud.io)
2. Create account and organization
3. Create new project
4. Get the token from your account settings
5. Add to GitHub secrets as `SONAR_TOKEN`

### **GITHUB_TOKEN** (Usually auto-available)
- This is automatically provided by GitHub Actions

## 🌿 **Step 4: Set Up Branch Structure**

### **Create Develop Branch**
```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/calculator-api.git
cd calculator-api

# Create and push develop branch
git checkout -b develop
git push origin develop

# Set develop as default branch (optional)
# Go to Settings → Branches → Default branch → Select develop
```

### **Branch Protection Rules**
1. Go to Settings → Branches
2. Add rule for `develop`:
   - ✅ "Require a pull request before merging"
   - ✅ "Require status checks to pass before merging"
   - ✅ "Require branches to be up to date before merging"

3. Add rule for `main`:
   - ✅ "Require a pull request before merging"
   - ✅ "Require status checks to pass before merging"
   - ✅ "Require branches to be up to date before merging"
   - ✅ "Restrict pushes that create files"

## 📝 **Step 5: Push Your Code**

```bash
# Add all files
git add .

# Initial commit
git commit -m "feat: initial calculator API with CI/CD pipeline"

# Push to develop
git push origin develop

# Create PR from develop to main
# Go to GitHub and create Pull Request: develop → main
```

## 🎯 **Step 6: Test the Workflow**

### **Create a Feature Branch**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/test-feature

# Make a small change to any file
echo "# Test comment" >> README.md

# Commit with conventional commit format
git add .
git commit -m "feat: add test comment to README"
git push origin feature/test-feature
```

### **Create PR to Develop**
1. Go to GitHub → Pull requests
2. Click "New pull request"
3. Base: `develop` ← Compare: `feature/test-feature`
4. Create PR
5. **Watch the CI run and auto-deploy to Development**

### **Create PR to Main**
1. Go to Pull requests
2. Click "New pull request"
3. Base: `main` ← Compare: `develop`
4. Create PR
5. **Watch the CI run and release-please create a release PR**

## 🔄 **Step 7: Complete the Release Cycle**

### **Merge Release PR**
1. Go to the release PR created by release-please
2. Review the changes (version bump + changelog)
3. Merge the PR
4. **Watch the new tag creation and UAT deployment**

### **Approve Production Deployment**
1. Go to Actions → Release and Deploy
2. Find the production deployment job
3. Click "Review deployments"
4. Approve the production deployment
5. **Watch the final production deployment**

## 📊 **What You'll See in Action**

### **Feature Branch**
- ✅ CI runs automatically
- ✅ Tests pass
- ✅ Ready for PR

### **PR to Develop**
- ✅ CI runs on PR
- ✅ All checks pass
- 🚀 **Auto-deploy to Development Environment**
- ✅ Can merge to develop

### **PR to Main**
- ✅ CI runs on PR
- ✅ Integration tests pass
- 🚀 **Release-please creates release PR**
- ✅ Can merge to main

### **Release Process**
- 🏷️ **New tag created** (e.g., v1.1.0)
- 🚀 **Auto-deploy to UAT**
- 🔒 **Production waits for approval**
- ✅ **Manual approval deploys to Production**

## 🎉 **Congratulations!**

You now have a complete CI/CD pipeline that demonstrates:
- **Pull Request workflows**
- **GitHub Environments**
- **Automated releases with release-please**
- **Semantic versioning**
- **Environment-based deployments**

## 🔧 **Troubleshooting**

### **CI Not Running**
- Check if workflows are in `.github/workflows/` directory
- Ensure branch names match workflow triggers
- Check GitHub Actions permissions

### **Release-please Not Working**
- Verify `.release-please-config.json` exists
- Check `.github/release-please.yml` workflow
- Ensure conventional commit format is used

### **Environment Deployments Failing**
- Check environment names match workflow files
- Verify environment protection rules
- Check required secrets are set

## 📚 **Next Steps**

1. **Experiment with different commit types**:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `test:` for tests

2. **Try different environments**:
   - Add more environments
   - Customize protection rules
   - Add deployment notifications

3. **Extend the pipeline**:
   - Add more quality gates
   - Integrate with other tools
   - Customize deployment logic

Happy learning! 🚀
