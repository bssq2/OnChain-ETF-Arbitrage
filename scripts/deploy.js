const hre = require("hardhat");

async function main() {
  // 1. Deploy ZkProofVerifier
  const ZkProofVerifier = await hre.ethers.getContractFactory("ZkProofVerifier");
  const zkVerifier = await ZkProofVerifier.deploy();
  await zkVerifier.deployed();
  console.log("ZkProofVerifier deployed to:", zkVerifier.address);

  // 2. Deploy ArbitrageEngine
  // For demonstration: pass dummy addresses for aavePool and chainlinkOracle
  const ArbitrageEngine = await hre.ethers.getContractFactory("ArbitrageEngine");
  const arbEngine = await ArbitrageEngine.deploy(
    "0x0000000000000000000000000000000000000000", // aavePoolAddress placeholder
    "0x0000000000000000000000000000000000000001"  // chainlinkOracle placeholder
  );
  await arbEngine.deployed();
  console.log("ArbitrageEngine deployed to:", arbEngine.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});