// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RegulatoryCompliance
 * @author Samson Boicu
 *
 * @notice Stub for FINRA/SEC checks + audit trail.
 *         Real implementation should query a compliance oracle.
 */
abstract contract RegulatoryCompliance {
    uint256 public lastTradeBlock;

    // FINRA Rule 5320 stub
    function isCompliant() public view returns (bool) {
        return true;  // always pass in demo
    }

    // Audit event — could be extended for ERC‑20 style logs
    event AuditTrail(address indexed trader, uint256 timestamp);

    function _logTrade() internal {
        emit AuditTrail(msg.sender, block.timestamp);
        lastTradeBlock = block.number;
    }
}